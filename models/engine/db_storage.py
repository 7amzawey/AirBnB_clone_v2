#!/user/bin/python3
"""
this module is for creating a new engine DBStorage
"""
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

HBNB_MYSQL_USER = getenv('HBNB_MYSQL_USER')
HBNB_MYSQL_PWD = getenv('HBNB_MYSQL_PWD')
HBNB_MYSQL_HOST = getenv('HBNB_MYSQL_HOST')
HBNB_ENV = getenv('HBNB_ENV')


class DBStorage:
    """this class is an engine class"""

    self.__engine = None
    self.__session = None

    def __init__(self):
        self.__engine = create_engine(
                f'mysql+mysqldb:
                //{HBNB_MYSQL_USER}:
                {HBNB_MYSQL_PWD}@localhost:3306/{HBNB_MYSQL_HOST}',
                pool_pre_ping=True)

        Session = sessionmaker(bind=engine)
        session = Session()

        if HBNB_ENV == 'test':
            session.delete().all()

    def all(self, cls=None):
        session.query(self.__session).all()
        if (cls == None):
            session.query(type(for obj in self.__session))
            
        cls_dict = {k: v for k,
                            v in self.__objects.items()}
                return cls_dict

	def new(self, obj):
       self.all().update(self.__objects)

    def save(self, obj):

