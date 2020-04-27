#!/usr/bin/env python3

import connexion

from ni_nfvo import encoder


def main():
    app = connexion.App(__name__, specification_dir='./swagger/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'NI-NFVO'})
    app.run(port=8181)


if __name__ == '__main__':
    main()
