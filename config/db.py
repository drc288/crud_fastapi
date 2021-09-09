from sqlalchemy import create_engine, MetaData
from os import getenv

user = "root" # getenv("DB_USER")
password = "toor" # getenv("DB_PASSWORD")

engine = create_engine(f"mysql+pymysql://{user}:{password}@localhost:3306/storedb")
my_metadata = MetaData()
connection = engine.connect()
