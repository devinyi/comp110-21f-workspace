"""This program compares numerical operators."""
left_hand_side: int = int(input("Left-hand side: "))
right_hand_side: int = int(input("Right-hand side: "))
exponent: int = left_hand_side**right_hand_side
division: float = left_hand_side / right_hand_side
integer_division: int = left_hand_side // right_hand_side
remainder: int = left_hand_side % right_hand_side
print(str(left_hand_side) + " ** " + str(right_hand_side) + " is " + str(exponent))
print(str(left_hand_side) + " / " + str(right_hand_side) + " is " + str(division))
print(str(left_hand_side) + " // " + str(right_hand_side) + " is " + str(integer_division))
print(str(left_hand_side) + " % " + str(right_hand_side) + " is " + str(remainder))

__author__ = "730397389"