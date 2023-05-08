# Create a program that will accept a word from a user and return the length of that word. 
# Make this program in a loop with option to exit when the use types in quit.

while True:
    a = input("Enter a word to see how many letters it has 'stop' to end the program: ")
    if a =="stop":
        break
    l = len(a)
    print("The word is these many letters long:", l)

