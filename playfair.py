import string

class playfair:

    def __init__ (self, key_in):
        self.key = key_in

    def getKey(self):
        return self.key

    def chunker(self, seq, size):
        assert len(seq) % 2 == 0, "sequence entered is odd"
        chunkedList = []
        while len(seq) > 1:
            chunk = (seq[0], seq[1])
            seq = seq[2:]
            chunkedList.append(chunk)
        return chunkedList

    def cleansInput(self, rawInput):
        # up-case letters
        # separate repeated letters with Xs
        
        rawInput = ''.join([c.upper() for c in rawInput if c in string.ascii_letters])
        cleanedInput = ""
        
        if len(rawInput) < 2:
            return rawInput

        for i in range(len(rawInput)-1):
            cleanedInput += rawInput[i]
            
            if rawInput[i] == rawInput[i+1]:
                cleanedInput += 'X'
        
        cleanedInput += rawInput[-1] # last char is ignored as we check rawInput[i+1] for being X

        if len(cleanedInput) & 1: # if odd (first binary digit is one), Then append X
            cleanedInput += 'X'

        return cleanedInput

    def generateTable(self, key):

        # J is not included as I/J are in the same cell
        alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
        table = []

        # copy key chars into the table if they are in `alphabet` ignoring duplicates and spaces
        for char in key.upper():
            if char not in table and char in alphabet:
                table.append(char)

        # fill the rest of the table in with the remaining alphabet chars
        for char in alphabet:
            if char not in table:
                table.append(char)

        return table

    def encode(self, plaintext):
        key = self.getKey()
        table = self.generateTable(key)
        plaintext = self.cleansInput(plaintext)
        ciphertext = ""

        for char1, char2 in self.chunker(plaintext, 2):
            row1 = int(table.index(char1)/5)
            col1 = table.index(char1) % 5

            row2 = int(table.index(char2)/5)
            col2 = table.index(char2) % 5

            if row1 == row2:
                ciphertext += table[row1*5+(col1+1)%5]
                ciphertext += table[row2*5+(col2+1)%5]
            elif col1 == col2:
                ciphertext += table[((row1+1)%5)*5+col1]
                ciphertext += table[((row2+1)%5)*5+col2]
            else: # intersection
                ciphertext += table[row1*5+col2]
                ciphertext += table[row2*5+col1]

        return ciphertext


    def decode(self, ciphertext):
        key = self.getKey()
        table = self.generateTable(key)
        plaintext = ""

        for char1, char2 in self.chunker(ciphertext, 2):
            row1 = int(table.index(char1)/5)
            col1 = table.index(char1) % 5

            row2 = int(table.index(char2)/5)
            col2 = table.index(char2) % 5

            if row1 == row2:
                plaintext += table[row1*5+(col1-1)%5]
                plaintext += table[row2*5+(col2-1)%5]
            elif col1 == col2:
                plaintext += table[((row1-1)%5)*5+col1]
                plaintext += table[((row2-1)%5)*5+col2]
            else: # intersection
                plaintext += table[row1*5+col2]
                plaintext += table[row2*5+col1]

        return plaintext