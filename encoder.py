import random
import string

class Encoder():
    def __init__(self) -> None:
        self.chars = string.digits + string.ascii_letters
        self.charsLen = len(self.chars)

    def makeSeed(self) -> str:
        # Shuffles seed
        seed = "".join(set(self.chars))
        '''
        random.shuffle(seed)

        # Makes seed a str
        seed = str(seed)
        '''

        self.seed: str = seed
        print(f"Seed: {seed}")

        return seed

    def encode(self, data: str) -> str:
        encodedData = ""
        for char in data:
            encodedChar = self.seed[self.chars.index(char)]
            encodedData += encodedChar

        return encodedData
    
    def decode(self, data: str) -> str:
        decodedData = ""
        for char in data:
            decodedChar = self.chars[self.seed.index(char)]
            decodedData += decodedChar

        return decodedData


encoder = Encoder()


encoder.makeSeed()

print(encoder.encode("hello"))
print(encoder.decode(encoder.encode("hello")))