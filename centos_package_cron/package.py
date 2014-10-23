from db_base import Base
from sqlalchemy import Column, Integer, String, Date, Numeric, ForeignKey

class Package(Base):
    __tablename__ = 'notified_packages'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    version = Column(String)
    release = Column(String)
    arch = Column(String)
    repository = Column(String)
    
    def __init__(self,name,version,release,arch,repository):
        self.name = name
        self.version = version
        self.release = release
        self.arch = arch
        self.repository = repository
        
    def __str__(self):
        return "Package %s-%s-%s" % (self.name, self.version, self.release)
        
    def __repr__(self):
        return self.__str__()