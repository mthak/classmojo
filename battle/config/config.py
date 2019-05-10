import os

class Config():

    if os.getenv('LOCAL_DB') == "True":
        DATABASE_NAME = 'localhost'
    else:
        DATABASE_NAME = "bigbattle"
    DATABASE_HOST= "phx-p10y-build-meta.p10y.eng.nutanix.com"
    DATABASE_PORT = 27017
