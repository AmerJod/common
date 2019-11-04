from spiderlib.db import Column, Integer, String, relationship
from spiderlib.db.db_modules import Base
from spiderlib.db.utils import to_json


class Author(Base):
    """
       Author table
       - One to many with Quote table
    """

    __tablename__ = "authors"

    author_id = Column(Integer, primary_key=True)
    author_name = Column(String(50))
    date_of_birth = Column(String)
    city = Column(String(50))
    country = Column(String(50))
    description = Column(String)

    quotes = relationship("Quote", back_populates="author", lazy=False)

    def __repr__(self):
        return (
            f"<Author(author_name='{self.author_name}', date_of_birth='{self.date_of_birth}',"
            f" city='{self.city}' , country='{self.country}' ,description ='{self.description}' )>"
        )

    # It is an easy way to convert it to json
    @property
    def to_dict(self):
        return {
            "author_id": self.author_id,
            "author_name": self.author_name,
            "date_of_birth": self.date_of_birth,
            "city": self.city,
            "country": self.country,
            "description": self.description,
        }

    # Not in use at the moment - kept for future work
    @property
    def json(self):
        return to_json(self, self.__class__)
