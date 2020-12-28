from ..errors.NotFound import WordNotFoundException
from treelib import Tree
from ..helpers.converter import converter


class CharResult:
    def __init__(self, character, chin_dict):
        self._character = character
        self._chin_dict = chin_dict
    
    @property
    def character(self):
        return self._character

    @property
    def simplified(self):
        try:
            return self._chin_dict._lookup_word(self.character).simplified
        except WordNotFoundException:
            return None 
        
    
    @property
    def traditional(self):
        try:
            return self._chin_dict._lookup_word(self.character).traditional
        except WordNotFoundException:
            return None 
        
    def _pinyin(self, style):
        try:
            res_list = [res.pinyin for res in self._chin_dict.lookup_word(self.character)]
            if style == 'accented':
                return [converter(pin) for pin in res_list]
            return res_list
        except WordNotFoundException:
            return None 
    
    @property
    def pinyin(self):
        return self._pinyin(self._chin_dict.pinyin_style)
    
    @property
    def meaning(self):
        try:
            return self._chin_dict._lookup_word(self.character).meaning
        except WordNotFoundException:
            return None
    
    def __repr__(self):
        return f'{self.__class__.__name__}({self.character})'
    

    def tree(self):
        tree = Tree()
        tree.create_node(self.character, self)
        
        
        def recursive(parent, tree):
            for child in parent.components:
                tree.create_node(child.character, child, 
                                 parent=parent)
                if hasattr(child, 'components'):
                    recursive(child, tree)
                    
        if hasattr(self, 'components'):
            recursive(self, tree)
            
        tree.show()


class Radical(CharResult):
    @property
    def num_strokes(self):
        try: 
            return self._chin_dict._lookup_char(self.character).num_strokes
        except WordNotFoundException:
            return None


class BaseChar(CharResult):
    def __init__(self, character, num_strokes, radical, chin_dict):
        super().__init__(character, chin_dict)
        self._num_strokes = num_strokes
        self._radical = Radical(radical, chin_dict) if radical != '*' else Radical(character, chin_dict)

    @property
    def num_strokes(self):
        return self._num_strokes
    
    @property
    def radical(self):
        return self._radical


class Char(BaseChar):
    def __init__(self, character, num_strokes, first, 
                 second, radical, chin_dict):
        super().__init__(character, num_strokes, radical, chin_dict)
        self._first = first
        self._second = second

    @property
    def components(self):
        return [self._chin_dict._lookup_char(self._first), 
                self._chin_dict._lookup_char(self._second)]


class MultipleChar(CharResult):
    @property
    def components(self):
        return [self._chin_dict._lookup_char(char) for char in self.character]


class WordResult:
    def __init__(self, simplified, traditional, pinyin, meaning, 
                 chin_dict):
        self._simplified = simplified
        self._traditional = traditional
        self._pinyin = pinyin
        self._meaning = meaning
        self._chin_dict = chin_dict

    def __repr__(self):
        return f'WordResult({self.simplified})'

    def __str__(self):
        return f"Simplified: {self.simplified}\nTraditional: {self.traditional}\nPinyin: {self.pinyin}\nMeaning: {self.meaning}\n"
     
    @property
    def simplified(self):
        return self._simplified
    
    @property
    def traditional(self):
        return self._traditional

    def _pinyin_meth(self, style='numerical'):
        if style == 'accented':
            return converter(self._pinyin)
        return self._pinyin 

    @property
    def pinyin(self):
        return self._pinyin_meth(self._chin_dict.pinyin_style)        

    @property
    def meaning(self):
        return self._meaning

    
