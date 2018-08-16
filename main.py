import random


class Key:
    def __init__(self, key=''):
        if key == '':
            self.key = self.generate()
        else:
            self.key = key.lower()

    def generate(self):
        key = ''
        portion = ''
        characters = 'abcdefghijklmnopqrstuvwxyz0123456789'

        while True:
            while len(key) < 25:
                character = random.choice(characters) # pick a random character from the string above and ...
                key += character # append to th key
                portion += character
                if len(portion) == 4:
                    key += '-' # add a hyphen after every 4 characters to get the aaaa-bbbb-cccc-dddd-3333 format
                    portion = ''

            key = key[:-1]
            if Key(key).verify():
                return key
            else:
                key = ''

    def verify(self):
        total = 0
        main_character = self.key[0]  # get the first character in the generated string
        main_character_count = 0
        portions = self.key.split('-')
        for portion in portions:
            if len(portion) != 4:
                return False
            else:
                for character in portion:
                    # check for the occurrences of the first character
                    if character == main_character:
                        main_character_count += 1  # this keeps track of the number of times the first character appears
                    total += ord(character)

        # change this values to experiment more
        # NOTE:
        # 1. a higher main_character_count takes longer to execute since it means that the first character
        #    of the generated key has to appear more
        # 2. a very low main_character_count means the key is less secure since any random string would fit
        if total == 1772 and main_character_count == 4:
            return True
        return False

    # This function just defines what shows up in the terminal when you print the class
    # It's an equivalent of toString() in java
    def __str__(self):
        valid = 'Invalid key'
        if self.verify():
            valid = 'Valid key'
        return self.key.upper() + " : " + valid

if __name__ == "__main__":
    print(Key())