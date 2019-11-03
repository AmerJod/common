from sqlalchemy import Column, Integer, String, Date, ForeignKey, Table, PrimaryKeyConstraint, Boolean
from sqlalchemy.orm import relationship

from .utils import DBEncoderJson, DBEncoderDict

# Initialize logger for the DB module
# could be optmise ..
from spiderlib.logging import NewLogger
logger = NewLogger(logger_name='database', store_flag=True).get_logger()