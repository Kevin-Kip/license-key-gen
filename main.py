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
        check_digit_count = 0
        characters = 'abcdefghijklmnopqrstuvwxyz0123456789'

        while True:
            while len(key) < 25:
                character = random.choice(characters)
                key += character
                portion += character
                if len(portion) == 4:
                    key += '-'
                    portion = ''

            if Key(key).verify():
                return key
            else:
                print(key+": Invalid key")
                key = ''

    def verify(self):
        print("d")