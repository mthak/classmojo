from mongoengine import connect

from battle.config.config import Config

connect(
    Config.DATABASE_NAME,
    host=Config.DATABASE_HOST,
    port=Config.DATABASE_PORT
)
