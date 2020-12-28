## Project Description

Python library for manipulating WikiCommons Character Info and CEDICT.

## Main features

* Decompose Chinese characters into sub-components with tree-like structure
* Character data such as radical, stroke number and traditional/simplified form
* Word lookup for meaning and pronunciation

## Installation

chin-dict is available on PyPI at https://pypi.org/project/chinese-dict/0.2.0/

	pip install ChinDict
	
### Command line tools

To make sure chin-dict is working properly, try looking up a word using the command line

	chindict 钱
	---------------------------------------------
	Character: 钱
	Pinyin: ['Qian2', 'qian2']
	Meaning: ['surname Qian', 'coin', 'money', 'CL:筆|笔[bi3]', 'unit of weight, one tenth of a tael 兩|两[liang3]']

To see the tree structure, use -t flag

 	chindict 钱 -t
 	---------------------------------------------
	钱
	├── 戋
	│   ├── 一
	│   └── 戈
	│       ├── 丿
	│       └── 弋
	└── 钅

To lookup as a word instead of a character, use -w flag

	chindict 钱 -w
	-----------------------------
	Simplified: 钱
	Traditional: 錢
	Pinyin: Qian2
	Meaning: ['surname Qian']

	Simplified: 钱
	Traditional: 錢
	Pinyin: qian2
	Meaning: ['coin', 'money', 'CL:筆|笔[bi3]', 'unit of weight, one tenth of a tael 兩|两[liang3]']

	
To see the character's radical, use -r flag

	chindict 钱 -r
	---------------------------------------------
	金

### Python demo

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


