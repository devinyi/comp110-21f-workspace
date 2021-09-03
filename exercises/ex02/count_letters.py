"""Counting letters in a string."""

__author__ = "730397389"


# Begin your solution here...
letter = str(input("What letter do you want to search for?: "))
word = str(input("Enter a word: "))
i = 0
counter = 0
while i < len(word):
    if letter == word[i]:
        counter = counter + 1
        i = i + 1
    else:
        i = i + 1
print("Count:", counter)