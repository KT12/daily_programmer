# Challenge No 5 medium


def main():
    pass

def read_words():
    global wordlist
    wordlist = []
    tf = open('cav.txt')
    for word in tf.read().split():
        wordlist.append(word)
    wordlist = list(set(wordlist)) # removes duplicates
    return wordlist
    find_anagrams(wordlist)

def find_anagrams(wordlist):
    anagrams = []
    WL2 = wordlist
    for w in wordlist:
        for z in WL2:
            if len(w) != len(z): # filtering out words with diff len
                continue
            elif sorted(w) != sorted(z): # filtering out words composed of different letters
                continue
            elif w == z: # deleting same words - will happen once per loop
                WL2.remove(w)
            else:
                anagrams.extend([w, z]) # adding all other words
    anagrams = str(set(anagrams)) # remvoving duplicate words - not sure if necessary
    print(len(anagrams)) #generates a weird number
    print(anagrams)

if __name__ == '__main__':
    main()
