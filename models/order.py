from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String, DateTime
from config.db import meta, engine 

order = Table("orders", meta,
              Column("id", Integer, primary_key=True),
              Column("seller_id", Integer, ForeignKey("users.id")),
              Column("user_id", Integer, ForeignKey("users.id")),
              Column("product_id", Integer, ForeignKey("products.id")),
              Column("created_at", DateTime),
              Column("updated_at", DateTime)
              )
meta.create_all(engine)
