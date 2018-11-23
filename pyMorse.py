
# Morse Code to Text Convertor
# Chris Fleming
# 23 November 2018

'''
The software will receive text as an input and produce the equivalent message
in written morse code as the output
'''
# ToDo: Add all the text letters and morse code values to the dictionary.
dictionary = {'s':'...', 'o': '---'}

# Stores the output.
morse_string = []

text_string = input('Input text to convert to morse: ')

for letter in text_string:
    convert = dictionary[letter]
    morse_string.append(convert)

# Fix the output to remove the [' '] marks.
print(morse_string)
