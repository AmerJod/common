

from sqlalchemy.ext.declarative import DeclarativeMeta
from sqlalchemy.orm.collections import InstrumentedList

from spiderlib.db.db_modules.quote import Quote
from spiderlib.db.db_modules.author import Author
from spiderlib.db.db_modules.tag import Tag


import json

class DBEncoderJson(json.JSONEncoder):
    """
        Helper class to convert SQLAlchemy db objects into json
    """

    def default(self, obj):
        # if
        if isinstance(obj.__class__, DeclarativeMeta):
            # an SQLAlchemy class
            fields = {}
            _excluded_fields = ["metadata", "json", "dict", "to_dict"]

            # filter the field
            for field in [x for x in dir(obj) if not x.startswith('_') and x not in _excluded_fields]:
                data = obj.__getattribute__(field)
                try:
                    json.dumps(data) # this will fail on non-encodable values, like other classes
                    fields[field] = data
                except TypeError:
                    # object needs its own method (.to_dict)
                    if not isinstance(data, InstrumentedList):
                        fields[field] = data.to_dict
                    else:
                        # list of object
                        # NOTE: it goes down one level only,
                        fields[field] = []
                        for item in data:
                            fields[field].append(item.to_dict)

            # a json-encodable dict
            return fields

        return json.JSONEncoder.default(self, obj)


class DBEncoderDict(object):
    """
        Helper class to convert SQLAlchemy nested db objects into dict
    """

    @staticmethod
    def encode(obj) -> dict:
        """
            Converts SQLAlchemy nested db objects into dict
        """

        # if


        if isinstance(obj.__class__, DeclarativeMeta):
            # an SQLAlchemy class
            _dict = {}
            _excluded_fields = ["metadata", "json", "dict", "to_dict"]

            # filter the field
            for field in [x for x in dir(obj) if not x.startswith('_') and x not in _excluded_fields]:
                data = obj.__getattribute__(field)
                try:
                    json.dumps(data) # this will fail on non-encodable values, like other classes
                    _dict[field] = data
                except TypeError:
                    # object needs its own method (.to_dict)
                    if not isinstance(data, InstrumentedList):
                        _dict[field] = data.to_dict
                    else:
                        # list of object
                        # NOTE: it goes down one level only,
                        _dict[field] = []
                        for item in data:
                            _dict[field].append(item.to_dict)
            return _dict


    @staticmethod
    def list_to_dict(list_obj) -> dict:
        """
        Converts a list fof SQLAlchemy nested db objects into dict.
        """
        _dict = dict()
        for index, obj in enumerate(list_obj):
            _dict[index] = DBEncoderDict.encode(obj)

        return _dict

