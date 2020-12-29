import unittest
from chin_dict.chindict import ChinDict

class TestChinDict(unittest.TestCase):

    def test_word_lookup_single_result(self):
        cd = ChinDict()
        res = cd.lookup_word("马")
        meanings = []
        pinyins = []
        for item in res:
            meanings.extend(item.meaning)
            pinyins.append(item.pinyin)
        self.assertTrue('horse' in meanings)
        self.assertTrue('ma3' in pinyins)

    def test_word_lookup_multiple_results(self):
        cd = ChinDict()
        res = cd.lookup_word("发")
        meanings = []
        pinyins = []
        for item in res:
            meanings.extend(item.meaning)
            pinyins.append(item.pinyin)

        self.assertTrue(pinyins[0] != pinyins[1])

    def test_char_lookup(self):
        cd = ChinDict()
        res = cd.lookup_char("好")

        self.assertTrue(len(res.components) == 2)
        self.assertTrue("good" in res.meaning)
        self.assertTrue("hao3" in res.pinyin)

    def test_traditional(self):
        cd1 = ChinDict(charset='traditional')
        res1 = cd1.lookup_word("說")[0].meaning
        
        cd2 = ChinDict(charset='simplified')
        res2 = cd2.lookup_word("说")[0].meaning

        self.assertTrue(res1 == res2)

    def test_numerical(self):
        cd = ChinDict(pinyin_style='accented')
        res = cd.lookup_char("好")
        
        self.assertTrue('hǎo' in res.pinyin)




if __name__ == '__main__':
    unittest.main()