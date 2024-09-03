
# This program accepts a text input from the user
# and calls a recursive function that reverses the string
# then prints the string to the user in reverse.


def reverseTheText():

    # Accepts the text input from the user.
    text = input("Please input a word to reverse it: ")
    
    # Converts the string to a list of characters.
    reversedText = list(text)

    # Reverses the order of the list.
    reversedText.reverse()

    # Joins the reversed list of characters into a string.
    reversedText = ''.join(reversedText)
    
    print(" ")
    print("Reversed: " + reversedText)



reverseTheText()
