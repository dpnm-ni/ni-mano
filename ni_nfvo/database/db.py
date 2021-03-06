from tinydb import TinyDB, Query
from tinydb.operations import delete
from tinydb_serialization import Serializer, SerializationMiddleware

from datetime import datetime
from threading import Lock

from ni_nfvo.models.sfcr import Sfcr
from ni_nfvo.models.sfc import Sfc


class DateTimeSerializer(Serializer):
    OBJ_CLASS = datetime
    FORMAT = '%Y-%m-%dT%H:%M:%S.%f'

    def encode(self, obj):
        return obj.strftime(self.FORMAT)

    def decode(self, s):
        # return datetime.strptime(s, self.FORMAT)
        # return raw string because from_dict() method require datetime in string format
        return s


serialization = SerializationMiddleware()
serialization.register_serializer(DateTimeSerializer(), 'TinyDate')

db = TinyDB('ni_nfvo/database/db.json', storage=serialization)
sfcs = db.table('sfcs', cache_size=30)
sfcrs = db.table('sfcrs', cache_size=30)
sfcs_lock = Lock()
sfcrs_lock = Lock()
query = Query()


def sfcs_sync(func):
    def _func(*args, **kwargs):
        with sfcs_lock:
            func(*args, **kwargs)
            sfcs.clear_cache()

    return _func


def sfcrs_sync(func):
    def _func(*args, **kwargs):
        with sfcrs_lock:
            func(*args, **kwargs)
            sfcrs.clear_cache()

    return _func


@sfcs_sync
def insert_sfc(sfc):
    sfcs.insert(sfc.to_dict())


@sfcs_sync
def update_sfc(sfc):
    sfcs.upsert(sfc.to_dict(), query.id == sfc.id)


@sfcrs_sync
def update_sfcr(sfcr):
    sfcrs.upsert(sfcr.to_dict(), query.id == sfcr.id)


@sfcrs_sync
def insert_sfcr(sfcr):
    sfcrs.insert(sfcr.to_dict())


def get_sfc(id):
    return Sfc.from_dict(sfcs.get(query.id == id))


def get_sfcr(id):
    return Sfcr.from_dict(sfcrs.get(query.id == id))


def get_all_sfcs():
    return [Sfc.from_dict(sfc) for sfc in sfcs.all()]


def get_all_sfcrs():
    return [Sfcr.from_dict(sfcr) for sfcr in sfcrs.all()]


@sfcs_sync
def del_sfc(id):
    sfcs.remove(query.id == id)


@sfcrs_sync
def del_sfcr(id):
    sfcrs.remove(query.id == id)
