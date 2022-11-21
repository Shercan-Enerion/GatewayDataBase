from pymongo import MongoClient
from .var_env import access_token_BD, database_name


class BaseData():
    def __init__(self):
        self.__conn = MongoClient(
            "mongodb+srv://yess:"+access_token_BD+"@cluster0.wdzh1o3.mongodb.net/?retryWrites=true&w=majority")[database_name]['Variables']
        self.__dictGet = {}

    def sendData(self, data):
        self.__conn.insert_one(data)

    def readData(self, **kwargs):
        '''
        parameters:
        limit: limit of data
        type_limit: int'''

        if len(kwargs) > 0:
            # for key, value in kwargs.items():
            #     self.__dictGet[key] = value
            return self.__conn.find()
        else:
            return self.__conn.find()
