import os
import sys
from contextlib import contextmanager

import psycopg2
import psycopg2.extras
from psycopg2 import pool
from backend.logger_base import log
from dotenv import load_dotenv

# Cargar variables desde .env
load_dotenv()

class Conexion:
    _pool = None
    _MIN_CON = 1
    _MAX_CON = 20

    @classmethod
    def obtenerPool(cls):
        if cls._pool is None:
            try:
                db_host = os.environ.get('DB_HOST', '127.0.0.1')
                db_name = os.environ.get('DB_NAME', 'postgres')
                db_user = os.environ.get('DB_USER', 'postgres')
                db_password = os.environ.get('DB_PASSWORD', '')
                db_port = int(os.environ.get('DB_PORT', '5432'))

                conn_kwargs = dict(
                    host=db_host,
                    database=db_name,
                    user=db_user,
                    port=db_port,
                    cursor_factory=psycopg2.extras.DictCursor
                )
                if db_password:
                    conn_kwargs['password'] = db_password
                    log.debug('Usando autenticación con password.')
                else:
                    log.debug('Intentando conexión SIN password (requiere trust en pg_hba.conf).')

                log.debug(f'Creando pool: host={db_host} port={db_port} db={db_name} user={db_user}')
                cls._pool = pool.SimpleConnectionPool(
                    cls._MIN_CON, cls._MAX_CON, **conn_kwargs
                )
                log.debug(f'Creación del pool exitosa {cls._pool}')
                return cls._pool
            except Exception as e:
                log.error('Ocurrió un error al obtener el pool: %s', repr(e))
                sys.exit(1)
        else:
            return cls._pool

    @classmethod
    def obtenerConexion(cls):
        conexion = cls.obtenerPool().getconn()
        log.debug(f'Conexión obtenida del pool: {conexion}')
        return conexion

    @classmethod
    @contextmanager
    def obtener_conexion(cls):
        conexion = None
        try:
            conexion = cls.obtenerConexion()
            yield conexion
        finally:
            if conexion:
                cls.liberarConexion(conexion)

    @classmethod
    def liberarConexion(cls, conexion):
        cls.obtenerPool().putconn(conexion)
        log.debug(f'Regresamos la conexión al pool: {conexion}')

    @classmethod
    def cerrarConexion(cls):
        cls.obtenerPool().closeall()
