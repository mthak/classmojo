import os

class Config():

    if os.getenv('LOCAL_DB') == "True":
        DATABASE_NAME = 'localhost'
    else:
        DATABASE_NAME = "bigbattle"
    DATABASE_HOST= "springs.eng.data.com"
    DATABASE_PORT = 27017
