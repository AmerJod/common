from sqlalchemy import create_engine
from sqlalchemy.orm.exc import *
from sqlalchemy.orm import sessionmaker

from spiderlib.db.db_modules import Base
from spiderlib.db.db_modules import Quote, Tag, Author

from spiderlib.db import logger


class Database(object):
    """
        Database Class that handles all the db queries, connections
    """

    # The values of those depend on your setup
    def __init__(self, **config):

        __db_conn_string = self.__construct_connection_string(**config)
        self.engine = create_engine(__db_conn_string)
        self.connection = self.engine.connect()
        self._session = sessionmaker(bind=self.engine)()

        # Enable and disable lazy_load
        self._lazy_load = config.get("DATABASE_LAZY_LOAD", False)

        logger.debug("DB Instance connected")

    def __construct_connection_string(self, **config):
        """ Construct connection string """

        # TODO: rasie an error incase one of is are empty
        # Get the db connection details
        POSTGRES_URL = config.get("POSTGRES_URL")
        POSTGRES_USER = config.get("POSTGRES_USER")
        POSTGRES_PW = config.get("POSTGRES_PW")
        POSTGRES_DB = config.get("POSTGRES_DB")

        logger.debug("construct connection string")

        return f'postgresql://{POSTGRES_USER}:{POSTGRES_PW}@{POSTGRES_URL}/{POSTGRES_DB}'


    # Not in used yet
    # using property decorator
    # a getter function
    @property
    def lazy_load(self):
        return self._lazy_load

    def _create_tables(self):
        Base.metadata.create_all(self.engine)
        logger.debug("DB Instance has been created")

    def _drop_databae(self):
        Base.metadata.drop_all(self.engine)
        logger.debug("DB Instance has been dropped")

    def _recreate_database(self):
        Base.metadata.drop_all(self.engine)
        Base.metadata.create_all(self.engine)
        logger.debug("DB Instance has been recreated")

    def add(self, obj):
        """ Adds db object to the database then return the object """

        try:
            self._session.add(obj)
            self._session.commit()
            logger.debug("db instance has has been added to the database")
            return obj
        except Exception as error:
            logger.error(f"db instance has has been added to the database, Error: {error}")

    def query(self, obj, **kwargs):
        """
        Returns db objects
            Args:
                **kwargs
            Return:
                db objects
        """
        try:
            db_objs = self._session.query(obj).filter_by(**kwargs).all()
            logger.debug("Queried the db")
            return db_objs

        except NoResultFound as error:
            logger.error("Query selects no rows")
            return None

        except MultipleResultsFound as error:
            logger.error("Multiple rows are returned for a query that returns")
            return None

        except Exception as error:
            logger.error(f"db instance has has been added to the database, Error: {error}")


    def query_one(self, obj, **kwargs):
        """
        Returns only one object if exist.
            Args:
                **kwargs
            Return:
                db objects
         """

        try:
            db_obj = self._session.query(obj).filter_by(**kwargs).one()
            return db_obj

        except NoResultFound as error:
            return None

        except MultipleResultsFound as error:
            logger.error("Multiple rows are returned for a query that returns")
            return None

        except Exception as error:
            logger.error(f"Something went wrong, Error: {error}")

    def exist(self, obj, **kwargs):
        """
        Returns only one object if exist.
            Args:
                **kwargs
            Return:
               (Boolean, db_object)
         """

        try:
            db_obj = self._session.query(obj).filter_by(**kwargs).one()
            return (True, db_obj)

        except NoResultFound as error:
            return (False, None)

        except Exception as error:
            logger.error(f"Something went wrong, Error: {error}")

    # def get_or_create(self, model, **kwargs):
    #     try:
    #         # basically check the obj from the db, this syntax might be wrong
    #         object = self._session.query(model).filter(**kwargs).first()
    #         return object
    #     except DoesNotExistException:  # or whatever error/exception it is on SQLA
    #         pass
    #         # object = model()
    #         # # do it here if you want to save the obj to the db
    #         # return object