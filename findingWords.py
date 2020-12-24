import csv
"""
1. We want to traverse our trie with a bfs
2. Take all the values from the trie and check if they are a word


"""
def load_most_frequent_words():
    with open('unigram_freq.csv', newline="") as csvfile:
        list = csv.reader(csvfile,delimiter=" ",quotechar="|")
        most_frequent_words = []
        for row in list:
            row = row[0].split(",")
            row[0] = row[0][::-1]
            most_frequent_words.append(row)
        return most_frequent_words

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



    