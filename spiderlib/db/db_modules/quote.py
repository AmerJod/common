from spiderlib.db import Column, Integer, String, ForeignKey, relationship
from spiderlib.db.db_modules import association_table, Base
from spiderlib.db.utils import to_json


class Quote(Base):
    """
        Quote table
        - Many to many Tag table
        - Many to one with Author table
    """

    __tablename__ = "quotes"

    quote_id = Column(Integer, primary_key=True)
    text = Column(String)

    author_id = Column(Integer, ForeignKey("authors.author_id"))
    author = relationship('Author', back_populates='quotes')

    tags = relationship("Tag", secondary=association_table)

    def __repr__(self):
        return f"<Quote(text='{self.text}', author_id={self.text})>"


    # It is an easy way to convert it to json
    @property
    def to_dict(self):
        return {
            "quote_id": self.quote_id,
            "text": self.text,
            "author_id": self.author_id
        }

    # Not in use at the moment - kept for future work
    @property
    def json(self):
        return to_json(self, self.__class__)
