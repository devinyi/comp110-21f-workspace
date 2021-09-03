"""Repeating a beat in a loop."""

__author__ = "730397389"


# Begin your solution here...
beat = str(input("What beat do you want to repeat? "))
repeat = int(input("How many times do you want to repeat it? "))
i = 0
end_string: str = beat
if repeat <= 0:
    print("No beat...")
else:
    while i < repeat:
        end_string = beat + " " + end_string
        i = i + 1
print(end_string)