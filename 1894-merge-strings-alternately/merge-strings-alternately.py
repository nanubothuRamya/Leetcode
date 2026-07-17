class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        p=zip_longest(word1,word2,fillvalue="")
        return "".join(char1+char2 for char1,char2 in p)