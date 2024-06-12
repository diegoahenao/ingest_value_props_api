import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

USER = os.environ.get("SNOWFLAKE_USER")
PASSWORD = os.environ.get("SNOWFLAKE_PASSWORD")
ACCOUNT = os.environ.get("SNOWFLAKE_ACCOUNT")
WAREHOUSE = os.environ.get("SNOWFLAKE_WAREHOUSE")
DATABASE = os.environ.get("SNOWFLAKE_DATABASE")
SCHEMA = os.environ.get("SNOWFLAKE_SCHEMA")
ROLE = os.environ.get("SNOWFLAKE_ROLE")

DATABASE_URL = (
    f'snowflake://{USER}:{PASSWORD}@{ACCOUNT}/'
    f'{DATABASE}/{SCHEMA}?warehouse={WAREHOUSE}&role={ROLE}'
)

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()