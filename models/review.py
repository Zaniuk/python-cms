from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import Integer, String, DateTime
from config.db import meta, engine 

review = Table("reviews", meta,
              Column("id", Integer, primary_key=True),
              Column("name", String(255)),
              Column("description", String(255)),
              Column("user_id", Integer, ForeignKey("users.id")),
              Column("product_id", Integer, ForeignKey("products.id")),
              Column("created_at", DateTime),
              Column("updated_at", DateTime)
              )
meta.create_all(engine)
