class WordDictionary:

    def __init__(self):
        self.collection = defaultdict(set)

    def addWord(self, word):
        if word:
            self.collection[len(word)].add(word)
        
    def search(self, word):
        options = self.collection[len(word)]
        if word == '':
            return False
        if '.' not in word:
            return word in options
        
        for option in options:
            match = True
            
            for i, char in enumerate(word):                
                if word[i] != option[i] and word[i] != '.':
                    match = False
                    break
            if match:
                return True
        return False