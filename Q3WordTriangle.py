# Create a program that will prompt the user for a word, and return a 'word triangle'. For example, if the user types in the word "PYTHON", your program will output:
# P
# PY
# PYT
# PYTH
# PYTHO
# PYTHON


word = input("Enter a word: ")

for i in range(len(word)):
    print(word[:i+1].ljust(len(word)))

for i in range(len(word)-2, -1, -1):
    print(word[:i+1].ljust(len(word)))

#I dont know how to stop the pyramid at Python 