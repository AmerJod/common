
# the values of those depend on your setup
POSTGRES_URL  = '0.0.0.0:54320'
POSTGRES_USER = 'postgres' # 'postgres'
POSTGRES_PW   = 'pwd123456'
POSTGRES_DB   = 'db_postgres'

SQLALCHEMY_DATABASE_URI = f'postgresql://{POSTGRES_USER}:{POSTGRES_PW}@{POSTGRES_URL}/{POSTGRES_DB}'

# DB_URL = f'postgresql+psycopg2://{POSTGRES_USER}:{POSTGRES_PW}@{POSTGRES_URL}/{POSTGRES_DB}'



