from spiderlib.db import Column, Integer, String, Boolean
from spiderlib.db.db_modules import Base
from spiderlib.db.utils import to_json


class Tag(Base):
    """
        Tag table
        - Many to many with Quote table
    """
    __tablename__ = "tags"
    tag_id = Column(Integer, primary_key=True)
    tag = Column(String(64))
    top_ten = Column(Boolean, default=False)

    # Not in use at the moment - kept for future work
    @property
    def json(self):
        return to_json(self, self.__class__)

    # It is an easy way to convert it to json
    @property
    def to_dict(self):
        return {
            "tag_id": self.tag_id,
            "tag": self.tag,
            "top_ten": self.top_ten
        }

    def __repr__(self):
        return f"<Tag(title='{self.tag}')>"
