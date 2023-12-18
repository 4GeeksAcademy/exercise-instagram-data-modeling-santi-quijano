import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er


Base = declarative_base()

class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(100), unique=True, nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    password = Column(String(100), unique=True)

class Followers(Base):
    __tablename__ = 'followers'
    id = Column(Integer, primary_key=True)
    user_from = Column(Integer, ForeignKey('users.id'))
    user = relationship(Users)
    user_to = Column(Integer, ForeignKey('users.id'))
    user = relationship(Users)

class Posts(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    caption = Column(String(100))
    image_url = Column(String(255), unique=True, nullable=False)
    created_at = Column(String(100))
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship(Users)

class Media(Base):
    __tablename__ = 'media'
    id = Column(Integer, primary_key=True)
    type = Column(Integer)
    url = Column(String(100))
    post_id = Column(Integer, ForeignKey('posts.id'))
    post = relationship(Posts)
    
class Comments(Base):
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True)
    text = Column(String(255))
    created_at = Column(String(255))
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship(Users)
    post_id = Column(Integer, ForeignKey('posts.id'))
    post = relationship(Posts)

class Like(Base):
    __tablename__ = 'likes'
    id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey('posts.id'))
    post = relationship(Posts)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship(Users)




    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
