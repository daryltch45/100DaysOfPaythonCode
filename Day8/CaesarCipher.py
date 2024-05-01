import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesarCipher(text, shift):

    new_text = []
    for c in text:
        if c in alphabet:
            index = alphabet.index(c.lower())
            index = (index + shift) % 26
            new_text.append(alphabet[index])

    return ''.join(new_text)


while(True):
    operation = input('Type \'encode\' to encrypt or \'decode\' to decrypt: ')
    if operation == 'encode' or operation == 'decode':
        text = input('Type your message: ')
        try:
            shift = int(input('Type the shift number: '))
            if operation == 'encode':
                print('Here is the encrypted result: ', caesarCipher(text, shift))
            elif operation == 'decode':
                print('Here is the decrypted result: ', caesarCipher(text, -shift))

            reply = input('''Type 'yes' id ou want to continue and 'no' to exit: ''')
            if reply != 'yes':
                break
        except ValueError:
            print('Please enter a number')
    else:
        print('Entry is not valid. Type \'encode\' or \'decode\'')




