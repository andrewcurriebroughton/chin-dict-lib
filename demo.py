from chin_dict.chindict import ChinDict

cd = ChinDict()

char_result = cd.lookup_char("泪")

print()
print("泪 components:")
print()

for component in char_result.components:
    print(component.character + ":", component.meaning)

# 氵: ['"water" radical in Chinese characters (Kangxi radical 85), occurring in 没, 法, 流 etc', 'see also 三點水|三点水[san1 dian3 shui3]']
# 目: ['eye', 'item', 'section', 'list', 'catalogue', 'table of contents', 'order (taxonomy)', 'goal', 'name', 'title']

print()

word_result = cd.lookup_word("发")

print("Translations for 发:")
print()
for word in word_result:
    print(word)

# Simplified: 发
# Traditional: 發
# Pinyin: fa1
# Meaning: ['to send out', "to show (one's feeling)", 'to issue', 'to develop', 'to make a bundle of money', 'classifier for gunshots (rounds)']

# Simplified: 发
# Traditional: 髮
# Pinyin: fa4
# Meaning: ['hair', 'Taiwan pr. [fa3]']