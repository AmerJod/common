
import redis

class Redis(object):

    def __init__(self, host="", port=6379, password=None, socket_timeout=5, **kwargs):
        self.redis = redis.StrictRedis(host=host, port=port,db=0,password=password,
                                       socket_timeout=5,decode_responses=True, **kwargs)

    def __bool__(self):
        '''Test if an object currently exists'''

        return self.redis.exists(self.id)

    def __eq__(self, other):
        '''Tests if two redis objects are equal (they have the same key)'''

        return self.id == other.id

    def __str__(self):
        '''Return this object as a string for testing purposes.'''

        return self.id

    def delete(self):
        '''Delete this object from redis'''

        self.redis.delete(self.id)

    @staticmethod
    def decode_value(type, value):
        '''Decode a value if it is non-None, otherwise, decode with no arguments.'''

        if value == None:
            return type()
        else:
            return type(value)

    @staticmethod
    def encode_value(value):
        '''Encode a value using json.dumps, with default = str'''

        return str(value)

