def accent_letter(letter, tone):
    """
    Adds accent to a vowel

    Parameters
    ----------
    letter : TYPE
        DESCRIPTION.
    tone : TYPE
        DESCRIPTION.

    Returns
    -------
    TYPE
        DESCRIPTION.

    """
    d = {
        'a': ['ā', 'á', 'ǎ', 'à', 'a'],
        'e': ['ē', 'é', 'ě', 'è', 'e'],
        'i': ['ī', 'í', 'ǐ', 'ì', 'i'],
        'o': ['ō', 'ó', 'ǒ', 'ò', 'o'],
        'u': ['ū', 'ú', 'ǔ', 'ù', 'u'],
    }
    return d[letter][int(tone)-1]

def find_letter_to_accent(pin):
    if 'a' in pin:
        return 'a'
    if 'e' in pin:
        return 'e'
    if 'ou' in pin:
        return 'o'
    for l in pin[::-1]:
        if l in 'aeiou':
            return l
        
def convert_char(char):
    tone = char[-1]
    if tone.isalpha():
        return char
    
    accented_vowel = find_letter_to_accent(char)
    accented_word = char.replace(accented_vowel, 
                                 accent_letter(accented_vowel, tone))
    
    return accented_word[:-1]

def converter(wrd):

    chars = wrd.split(' ')
    
    accented_words = list(map(convert_char, chars))
    
    return ''.join(accented_words)

