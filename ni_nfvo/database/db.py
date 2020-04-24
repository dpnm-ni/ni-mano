from tinydb import TinyDB, Query
from tinydb.operations import delete
from tinydb_serialization import Serializer, SerializationMiddleware

from datetime import datetime

from ni_nfvo.models.sfcr import SFCR
from ni_nfvo.models.route import Route


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
routes = db.table('routes', cache_size=30)
sfcrs = db.table('sfcrs', cache_size=30)
query = Query()

def insert_route(route):
    routes.insert(route.to_dict())

def update_route(route):
    routes.upsert(route.to_dict(), query.id == route.id)

def update_sfcr(sfcr):
    sfcrs.upsert(sfcr.to_dict(), query.id == sfcr.id)

def insert_sfcr(sfcr):
    sfcrs.insert(sfcr.to_dict())

def get_route(id):
    return Route.from_dict(routes.get(query.id == id))

def get_sfcr(id):
    return SFCR.from_dict(sfcrs.get(query.id == id))

def get_all_routes():
    return [Route.from_dict(route) for route in routes.all()]

def get_all_sfcrs():
    return [SFCR.from_dict(sfcr) for sfcr in sfcrs.all()]

def del_route(id):
    routes.remove(query.id == id)

def del_sfcr(id):
    sfcrs.remove(query.id == id)
