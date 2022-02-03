import sys
sys.path.append('..')

import snowflake.connector
from configs.SnowflakeCredentials import USERNAME, PASSWORD, WAREHOUSE, ACCOUNT_IDENTIFIER, DATABASE, SCHEMA


# Create a snowflake connection
def createConnection(username = USERNAME,
                     password = PASSWORD,
                     warehouse = WAREHOUSE,
                     account = ACCOUNT_IDENTIFIER,
                     database = DATABASE,
                     schema = SCHEMA):

    return snowflake.connector.connect(
        user = username,
        password = password,
        account = account,
        warehouse = warehouse,
        database = database,
        schema = schema
    )


# query data from snowflake
def querySnowflake(queryText):
    with createConnection() as conn:
        cs = conn.cursor()
        try:
            cs.execute(queryText)
            return cs.fetchall()
        finally:
            cs.close()
