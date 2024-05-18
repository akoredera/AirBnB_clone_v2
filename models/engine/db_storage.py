from sqlalchemy import create_engine
"""Class for Database storage using MYSQL"""


class DBStorage:
    """Database Storage class"""
    __engine = None
    __session = None

    def __init__(self):
    """initialization method"""
    self.__engine = create_engine('mysql+mysqldb://HBNB_MYSQL_USER:HBNB_MYSQL_PWD@localhost/HBNB_MYSQL_DB', pool_pre_ping=True, echo=True)

    def all(self, cls=None):
    """query on the current database session"""
    self.__session 
