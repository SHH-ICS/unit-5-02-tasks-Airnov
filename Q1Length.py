# Create a program that will accept a word from a user and return the length of that word. 
# Make this program in a loop with option to exit when the use types in quit.

while True:
    a = input("Please enter a word (or type 'quit' to exit): ")
    if a == "quit":
        break
    l = len(a)
    print("The length of the word is:", l)

