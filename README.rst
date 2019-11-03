
- Author:   Amer Joudiah
- Date:     3/11/2019


``spiderlib``: A simple common lib for the API/spiders project :)
=================================================================

It is simple library (MVP version), that used to reduce code redundancy between multiple projects. and make the code easy to maintain.

Modules Included:
=================

1.   ``db``:
        - A single db interface to make connection to the db, and perform queries.
            Below you can see all the db models:

            .. code-block:: python

                class Author(Base):
                    """
                    Author table
                         - One to many with Ouote table
                    """
                        __tablename__ = "authors"
                        author_id = Column(Integer, primary_key=True)
                        author_name = Column(String(50))
                        date_of_birth = Column(String)
                        city = Column(String(50))
                        country = Column(String(50))
                        description = Column(String)
                        quotes = relationship("Quote", back_populates="author", lazy=False)


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
                        author = relationship("Author", back_populates="quotes")
                        tags = relationship("Tag", secondary=association_table)

                class Tag(Base):
                    """
                    Tag table
                        - Many to many with Quote table
                    """
                        __tablename__ = "tags"
                        tag_id = Column(Integer, primary_key=True)
                        tag = Column(String(64))
                        top_ten = Column(Boolean, default=False)


2.  ``logger``:
        - A single interface to deal with logging, multiple separated loggers can be created for each module.


    .. code-block:: python

        # Initialize logger for the DB module
        # could be optmise ..
        from spiderlib.logging import NewLogger
        logger = NewLogger(logger_name='database', store_flag=True).get_logger()