from pyMorse.encoding import MorseEncoding
# Morse Code to Text Convertor
# Chris Fleming
# 23 November 2018
def run():
    """
    The software will allow the receive text as an input and produce the equivalent message
    in written morse code as the output
    """
    print(MorseEncoding().convert(input("Enter text to convert to Morse: ")))

if __name__ == '__main__':
    run()
