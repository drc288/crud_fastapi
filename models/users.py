from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import my_metadata, engine

users = Table('users', my_metadata,
              Column("id", Integer, primary_key=True),
              Column("name", String(255)),
              Column("password", String(255)),
              Column("email", String(255))
              )

my_metadata.create_all(engine)
