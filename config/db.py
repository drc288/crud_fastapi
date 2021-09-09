from sqlalchemy import create_engine, MetaData
from os import getenv

user = "root"  # getenv("DB_USER")
password = "toor"  # getenv("DB_PASSWORD")
url = "localhost"
port = 3306
database = "storedb"

engine = create_engine(
    f"mysql+pymysql://{user}:{password}@{url}:{port}/{database}")
my_metadata = MetaData()
connection = engine.connect()
