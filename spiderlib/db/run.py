from spiderlib.db.database import Database

#  For testing purposes
POSTGRES_CONN = {
    "POSTGRES_URL": "0.0.0.0:54320",
    "POSTGRES_USER": "postgres",
    "POSTGRES_PW": "pwd123456",
    "POSTGRES_DB": "db_postgres"
}

if __name__ == '__main__':
    # logger = Logger('Spider').get_logger()
    # For testing
    # logger.error("3364")
    # logger.debug("Amer")
    # logger.info("INFO")
    # logger.critical("CRITICAL")
    db = Database(**POSTGRES_CONN)
    db._recreate_database()
