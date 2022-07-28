import random, string

class Codec:
    def __init__(self):
        self.store = {}
        
    def generateKey(self):
        return ''.join(random.choice(string.ascii_lowercase) for i in range(5))
    
    def getKey(self, shortUrl):
        return shortUrl[23:]

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        key = self.generateKey()
        while key in self.store:
            key = self.generateKey()
            
        self.store[key] = longUrl        
        return "https://goriberurl.com/" + key

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.store[self.getKey(shortUrl)]
        
