from sqlalchemy.ext.declarative import declarative_base

from spiderlib.db import Table, Column, Integer, ForeignKey

Base = declarative_base()

# Many to many relationship table 'quotes_tags'
association_table = Table(
    "quotes_tags",
    Base.metadata,
    Column("quote_id", Integer, ForeignKey("quotes.quote_id")),
    Column("tag_id", Integer, ForeignKey("tags.tag_id")),
)

from spiderlib.db.db_modules.author import Author
from spiderlib.db.db_modules.tag import Tag
from spiderlib.db.db_modules.quote import Quote
