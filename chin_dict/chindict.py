from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .classes.charresult import CharResult, BaseChar, Char, WordResult, \
    MultipleChar

from .errors.NotFound import WordNotFoundException

from .classes.models import Character, Word

from .helpers.cleaner import clean_db_res

import sys


class ChinDict:
    """
    Chinese dictionary instance
    Parameters
    ----------
    charset : str
        'simplified' or 'traditional' (default=simplified).
    pinyin_style : str
        'numerical' or 'accented' (default=numerical).


    """

    
    def __init__(self, charset='simplified', pinyin_style='numerical'):
        
        if charset not in ('simplified', 'traditional'):
            raise AttributeError("charset must be either \
                                 'simplified' or 'traditional'")
                                 
        if pinyin_style not in ('numerical', 'accented'):
            raise AttributeError("pinyin_style must be either \
                                 'numerical' or 'accented'")
                                 
        engine = create_engine('sqlite:///' + sys.prefix + '/data/hanlearn.db')        
        Session = sessionmaker(bind=engine, autoflush=False)
        
        self._session = Session()

        
        self.charset = charset
        self.pinyin_style = pinyin_style

        
    def lookup_char(self, char):
        """
        Lookup input in character decomposition database
    
        Parameters
        ----------
        char : str
            chinese character(s) to be searched for in the database.
    
        Returns
        -------
        CharacterType
            Variable return type based on searched character.
    
        """

        
        if len(char) > 1:
            return MultipleChar(char, self)
        
        db_res = self._session.query(Character).filter_by(character=char).first()

        if db_res is None:
            return CharResult(char, self)
        
        if db_res.second_character == '*':
            return BaseChar(db_res.character, db_res.num_strokes, 
                                  db_res.radical, self)

        return Char(db_res.character, db_res.num_strokes,
                          db_res.first_character, db_res.second_character,
                          db_res.radical, self)
    
    def lookup_word(self, char):
        """
        Lookup input in character semantics database
    
        Parameters
        ----------
        char : str
            chinese character(s) to be searched for in the database.
    
        Returns
        -------
        list
            List of dictionaries containing word details for each match in the database.
    
        """

        
        charset_map = {'simplified': 'simp', 'traditional': 'trad'}

        db_all = self._session.query(Word).filter(
            getattr(Word, charset_map[self.charset])==char).all()
        
        if len(db_all) == 0:
            raise WordNotFoundException(f"No results for word: '{char}'")

        
        for res in db_all:
            clean_db_res(res)
                
        return_list = [WordResult(res.simp, res.trad, res.pinyin, res.meaning, self) for res in db_all]
        
        return return_list
    
    def _lookup_char(self, char):
        """
        Interal method that searches decomposition database
    
        Parameters
        ----------
        char : str
            chinese character(s) to be searched for in the database.
    
        Returns
        -------
        CharResult
            Variable return type based on searched character.
    
        """
    
        db_res = self._session.query(Character).filter_by(character=char).first()

        if db_res is None:
            return CharResult(char, self)
        
        if db_res.second_character == '*':
            return BaseChar(db_res.character, db_res.num_strokes, 
                                  db_res.radical, self)

        return Char(db_res.character, db_res.num_strokes,
                          db_res.first_character, db_res.second_character,
                          db_res.radical, self)
        

    
    def _lookup_word(self, char):
        """
        Interal method that searches semantic database
    
        Parameters
        ----------
        char : str
            chinese character(s) to be searched for in the database.
    
        Returns
        -------
        List
            list of WordResult objects for each interpretation of character
    
        """


        charset_map = {'simplified': 'simp', 'traditional': 'trad'}
        
        db_all = self._session.query(Word).filter(
            getattr(Word, charset_map[self.charset])==char).all()
        
        if len(db_all) == 0:
            raise WordNotFoundException(f"No results for word: '{char}'")
            
        pinyin = []
        meaning = []
        simplified = []
        traditional = []
        
        for res in db_all:
            clean_db_res(res)

        for res in db_all:
            pinyin.append(res.pinyin)
            meaning.extend(res.meaning)
            simplified.append(res.simp)
            traditional.append(res.trad)


                    
        result = WordResult(simplified, traditional, pinyin, meaning, self)
        
        return result
    
