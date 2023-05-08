# Create a program that will accept a word and output the word one letter at a time in reverse.

string = input("Enter a word to see how it looks like in reverse: ")
reversed_string = string[::-1]
for letter in reversed_string:
    print(letter)

