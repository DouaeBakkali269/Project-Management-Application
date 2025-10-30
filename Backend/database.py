# SO SQLAlchemy is  a Python Library that helps you interact with databases in a more convenient and Pythonic way

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import settings

# create_engine is a method that creates a connection to the database.
engine = create_engine(settings.DATABASE_URL)

# sessionmaker: This is a factory function to create session objects, which are used to interact with the database (like querying, adding, or deleting rows).
# autocommit=False: The session will not automatically commit changes to the database. You need to call session.commit() manually.
# autoflush=False: SQLAlchemy won’t automatically push changes to the database before a query. This avoids unexpected behavior sometimes.
#bind=engine: This session will use the engine we created to connect to the database.

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind= engine )

Base = declarative_base() # used to define models(tables) in a pythonic way , we will create classes that represent database tables.
