
print('Welcome to More Code converter')
MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}


def encrypt(message):
    morse_message = ''
    if message != '':
        for char in message:
            if char == ' ':
                continue
            try:
                morse_message += MORSE_CODE_DICT[char.upper()] + ' '
            except KeyError as e:
                print(f'Invalid character used {e}, please use only allowed characters to craft encrypted message.')
                quit()
        return morse_message

def decrypt(message):
    encrypted_message = message
    result = ''
    if encrypted_message != '':
        code = encrypted_message.split(' ')
        for char in code:
            if char == '/': ### look for possible spaces
                result += ' '
            for key,value in MORSE_CODE_DICT.items(): ### finding the letters based on the Morse Code characters.
                if char==value:
                    result += key
    return result


user_choice = input('Do you want to encrypt or decrypt the message using Morse Code? ').lower()
def main(choice):
    if user_choice == 'encrypt':
        user_input = input('Enter the message you want to be encrypted: ')
        print(encrypt(message=user_input))
    elif user_choice == 'decrypt':
        user_input = input('Enter the message you want to be decrypted: ')
        print(decrypt(message=user_input))
    else:
        print('Invalid Input')
if __name__ == '__main__':
    main(choice=user_choice)
