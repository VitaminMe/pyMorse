
# Morse Code to Text Convertor
# Chris Fleming
# 23 November 2018
def run():
    """
    The software will allow the receive text as an input and produce the equivalent message
    in written morse code as the output
    """
    dictionary = {'s':'...', 'o': '---'}
    morse_string = (' ')
    text_string = 'sos'

    for letter in text_string:
        convert = dictionary[letter]
        morse_string = morse_string + convert

    print(morse_string)

if __name__ == '__main__':
    run()
