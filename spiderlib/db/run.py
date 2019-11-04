from spiderlib.db.database import Database

#  For testing purposes
POSTGRES_CONN = {
    "POSTGRES_URL": "localhost:54320",
    "POSTGRES_USER": "postgres",
    "POSTGRES_PW": "postgres",
    "POSTGRES_DB": "postgres"
}

if __name__ == '__main__':
    db = Database(**POSTGRES_CONN)
    print(POSTGRES_CONN)
    db._recreate_database()
