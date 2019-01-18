import pymongo as pymongo
from config import *

######################### 调取mongoDB存储 ################################
def save_to_mongo(tableName,result):
    client = pymongo.MongoClient(MONGO_URL)  ##  连接mongoDB客户端
    db = client[MONGO_DB]  ##  连接数据库
    if db[tableName].insert(result):
        print('存储到MongoDB成功', result)
        return True
    print('存储到MongoDB失败', result)
######################### 调取mongoDB存储 ################################