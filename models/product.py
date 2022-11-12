from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String, DateTime
from config.db import meta, engine 

product = Table("products", meta,
              Column("id", Integer, primary_key=True),
              Column("name", String(255)),
              Column("description", String(255)),
              Column("price", Integer),
              Column("seller_id", Integer, ForeignKey("users.id")),
              Column("created_at", DateTime),
              Column("updated_at", DateTime)
              )
meta.create_all(engine)
