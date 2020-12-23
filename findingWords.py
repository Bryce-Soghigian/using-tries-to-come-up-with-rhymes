"""
1. We want to traverse our trie with a bfs
2. Take all the values from the trie and check if they are a word


"""


def load_words():
    with open('words_alpha.txt') as word_file:
        valid_words = set(word_file.read().split())

    return valid_words



def getWordsFromTextFile():
    """
    This function adds all the words from words.txt and throws them into a set();
    """
    WORDLIST_FILENAME = "words.txt"
    print("LOADING WORDS")
    words = open(WORDLIST_FILENAME,"r")
    line = words.readline()
    wordList = line.split()
    wordSet= set()
    print(" ",len(wordList),"Words in file")
    for item in wordList:
        wordSet.add(item)
    
    return wordSet



    