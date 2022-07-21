import sqlalchemy.exc
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from termcolor import colored

from dotenv import load_dotenv
import os

load_dotenv()
engine = None
try:
    engine = create_engine(os.getenv('DB_URL'))

except sqlalchemy.exc.ArgumentError as exception:
    print(colored(text='Неправильный формат ссылки к бд', color='red', attrs=['bold']))
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
