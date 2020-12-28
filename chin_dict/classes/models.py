from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class Word(Base):
    """Model for entries in dictionary"""
    
    __tablename__ = 'words'
    
    id = Column(Integer, primary_key=True)
    simp = Column(String)
    trad = Column(String)
    pinyin = Column(String)
    meaning = Column(String)
    
    
class Character(Base):
    """Model for entries in dictionary"""
    
    __tablename__ = 'characters'
    
    id = Column(Integer, primary_key=True)
    character = Column(String)
    num_strokes = Column(String)
    composition = Column(String)
    first_character = Column(String)
    num_strokes_first = Column(String)
    second_character = Column(String)
    num_strokes_second = Column(String)
    input_code = Column(String)
    verified = Column(String)
    radical = Column(String)
    
    def __repr__(self):
        return self.character
