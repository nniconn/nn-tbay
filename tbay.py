from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, Float


engine = create_engine('postgresql://ubuntu:thinkful@localhost:5432/tbay')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()




class Item(Base):
    __tablename__ = "items"
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)
    start_time = Column(DateTime, default=datetime.utcnow)
    
    print('items table created')


class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)
    


#below code not working commented it out for now
# def __init__(self, username, password):
    # self.username = bknowles
    # self.password = lemonade
    
    # def __repr__(self):
        
        
# def __repr__(self):
    # self.username = bknowles
    # self.password = lemonade
    # session.add(bknowles)
    # session.commit()
    
        
    # return "<User('%s', '%s')>" % (self.username, self.password)
    
    
print('users table created')
    


class Bid(Base):
    __tablename__ = "bids"
    
    id = Column(Integer, primary_key=True)
    price = Column(Float, primary_key=True)
    
    print('bid table created')
    
    
    
    

Base.metadata.create_all(engine)


beyonce = User()
beyonce.username = "bknowles"
beyonce.password = "lemonade"
session.add(beyonce)
session.commit()

hendrix = User()
hendrix.username = "jhendrix"
hendrix.password = "purple haze"
session.add(hendrix)
session.commit()

guitar = Item()
guitar.name = "Fender"
guitar.description = "Black Fender Stratocaster 1969"
session.add(guitar)
session.commit()

microphone = Item()
microphone.name = "Shure"
microphone.description = "Gold Shure Microphone"
session.add(microphone)
session.commit()
