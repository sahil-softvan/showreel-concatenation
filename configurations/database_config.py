from configurations.knit_services_config import SecretManager, AppServices
import urllib.parse
from pymongo.errors import ConnectionFailure
from pymongo import MongoClient
# from app.core.loggin import MyLogger

# logger = MyLogger().get_logger("knit_db")

secret_manager = SecretManager()
secret_details = secret_manager.get_secret_manager_details()
configure = AppServices.get_config()
MONGODB_URL = configure.get('KNIT_DATABASE_CONNECTION', 'mongodb_url')


def get_client(alias):

    username = urllib.parse.quote_plus(secret_details['db_username'])
    password = urllib.parse.quote_plus(secret_details['db_password'])
    endpoint = secret_details[alias.upper() + "_PUB_DB_ENDPOINT"]
    client = MongoClient(MONGODB_URL.format(
        username,
        password,
        endpoint), connect=False)

    try:
        # The ismaster command is cheap and does not require auth.
        client.admin.command('ismaster')
        # logger.info("client : {}".format(client))

    except ConnectionFailure as con_exc:
        # logger.error("Found error while connecting to the mongo db : {}".format(con_exc))
        raise Exception("Can't able to connect with database : {}".format(con_exc))

    return client
