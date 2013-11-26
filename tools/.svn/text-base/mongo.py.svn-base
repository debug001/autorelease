#!/usr/bin/env python
#encoding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class Mongo:
    def __init__(self, **config):
        #===========argument===========
        # host, port, database, table

        config.setdefault('port', 27017)

        self.host     = config['host']
        self.port     = config['port']
        self.database = config['database']
        self.table    = config['table'] 
        Mongo.connect(self)

    def connect(self):
        import pymongo
        connection = pymongo.Connection(self.host, self.port)
        db = eval("connection." + self.database)
        collection = eval("db." + self.table)
        self.collection = collection

    def find(self, **sql):                #dict key=value
        data = self.collection.find(sql)
        return data

    def find_count(self, **sql):
        num = self.collection.find(sql).count()
        return num

    def insert(self, **sql):
        self.collection.insert(sql)

    def update(self, **sql):             #mongo_conn.update(condition={'ip':'122.4.74.3'}, data={'data':'value'})
        if not sql.has_key('condition') or not sql.has_key('data'):
            raise Exception('condition or data not in arguments!')
        return self.collection.update(sql['condition'],{"$set":sql['data']})

    def remove(self, **sql):
        self.collection.remove(sql)

    def drop(self):
        return self.collection.drop()




