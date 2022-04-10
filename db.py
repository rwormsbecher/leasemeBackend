import os
import urllib

import databases
import sqlalchemy

host_server = os.environ.get('host_server', 'localhost')
db_server_port = urllib.parse.quote_plus(str(os.environ.get('db_server_port', '5432')))
database_name = os.environ.get('database_name', 'leaseme')
db_username = urllib.parse.quote_plus(str(os.environ.get('db_username', 'postgres')))
db_password = urllib.parse.quote_plus(str(os.environ.get('db_password', 'secret')))
# DATABASE_URL = 'postgresql://{}:{}@{}:{}/{}?sslmode=require'.format(db_username, db_password, host_server,
# db_server_port, database_name)

DATABASE_URL = f"postgresql://{db_username}:{db_password}@{host_server}:{db_server_port}/{database_name}?sslmode=require"
database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()
