from Trie import PrefixTree
from findingWords import load_most_frequent_words
import secrets
"""
Functions in main
1. getWordsWithMatchingSuffix
2. getMostCommon Suffix

"""


def fetchKthMostCommonSuffixOfLengthN(k,n):
    #Step 1 Count all the suffixes of length n
    ## Step 1.a Loop through wordListInMatchingSuffix and break each word apart.
    ## CHeck if a word suffix has allready been counted
    freq = {}
    wordList = load_most_frequent_words()
    for i in range(len(wordList)):
        word = wordList[i][0][::-1]
        suffix = word[-n:]
        if suffix in freq.keys():
            freq[suffix] = freq[suffix] + 1
        else:
            freq[suffix] = 1
    dictlist = []
    for key, value in freq.items():
        temp = [key,value]
        dictlist.append(temp)
    dictlist.sort(key=lambda x:x[1])
    listOfKValues = dictlist[-k:]
    output = []
    for val in listOfKValues:
        output.append(val[0])
    return output

def getWordsWithMatchingSuffix(suffix,maxWordLength):
    """
    Purpose of getWordsWithMatchingSuffix
    I want this code to find me words that rhyme.
    1. Init a trie with all the words from words_alpha.txt
    2. Go through and reverse all the words so you can read them
    3 return list of words that match that suffix in the english language
    """


    """========= STEP 1==========="""
    wordListInMatchingSuffix = load_most_frequent_words()
    wordTrie = PrefixTree()
    print("Loading Words into Trie...")

    for word in wordListInMatchingSuffix:

        if(len(word[0])>4 and len(word[0])<maxWordLength):
            if word[1]:
                if int(float(word[1])) > 641999:
                    wordTrie.insert(word[0])

    #Step 2
    wordsThatMatchSuffix = wordTrie.starts_with(suffix[::-1])
    for i in range(len(wordsThatMatchSuffix)):
        wordsThatMatchSuffix[i] = wordsThatMatchSuffix[i][::-1]
    #Step 3
    print("returning words that match your suffix from our dataset")
    return wordsThatMatchSuffix




# print(secrets.choice(start_and_end_suffix))
start_and_end_suffix = fetchKthMostCommonSuffixOfLengthN(10,4)
starting_word = getWordsWithMatchingSuffix(secrets.choice(start_and_end_suffix),12)
ending_word = getWordsWithMatchingSuffix(secrets.choice(start_and_end_suffix),12)


for i in range(10):
    print(f"{starting_word[i]}_____________________________{ending_word[i]}")













