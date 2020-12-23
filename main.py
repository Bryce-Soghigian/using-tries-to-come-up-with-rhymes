from Trie import PrefixTree
from findingWords import load_words
def getWordsWithMatchingSuffix(suffix,maxWordLength):
    """
    Purpose of getWordsWithMatchingSuffix
    I want this code to find me words that rhyme.
    1. Init a trie with all the words from words_alpha.txt
    2. Go through and reverse all the words so you can read them
    3 return list of words that match that suffix in the english language
    """


    """========= STEP 1==========="""
    wordTrie = PrefixTree()
    wordList = load_words()
    for word in wordList:
        if(len(word) > maxWordLength):
            pass
        else:
            wordTrie.insert(word)

    #Step 2
    wordsThatMatchSuffix = wordTrie.starts_with(suffix)
    for i in range(len(wordsThatMatchSuffix)):
        wordsThatMatchSuffix[i] = wordsThatMatchSuffix[i][::-1]
    #Step 3
    return wordsThatMatchSuffix

endWithCh = getWordsWithMatchingSuffix("he",5)
endWithEp = getWordsWithMatchingSuffix("hct",5)
print(endWithCh)
print(endWithEp)




