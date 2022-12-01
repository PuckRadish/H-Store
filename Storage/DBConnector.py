import psycopg2 ##导入
import leveldb
import py2neo
from py2neo import Graph
from influxdb import InfluxDBClient

'''
    PostgreSQL connector module
'''
def pgConnect():
    conn = psycopg2.connect(database="db_test", user="postgres", password="12345678", host="127.0.0.1", port="5432")
    print('PostgreSQL connection successful!')
    return conn
'''
    LevelDB connector module
'''
def leveldbConnect():
    db = leveldb.LevelDB('./db')
    db.Put('hello', 'world')
    print(db.Get('hello'))


def GraphConnect():
    graph = Graph('',username="",password="")
    return graph


def influxConnect():
    conn = InfluxDBClient('127.0.0.1','8086','u_wyk13195','p_wyk13195','my_monitor')
    return conn
