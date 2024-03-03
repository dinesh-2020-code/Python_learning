
letters = "abcdefghijklmnopqrstuvwxyz"
backwards = letters[25:0:-1]
print(backwards)   # prints "zyxwvutsrqponmlkjihgfedcb"

print(letters[25::-1]) # prints "zyxwvutsrqponmlkjihgfedcba"

print(letters[::-1]) # prints "zyxwvutsrqponmlkjihgfedcba"
print(letters[-22::-1])  #prints "edcba"

print(letters[:-9:-1])  #prints last 8 characters in reverse order.

# print last 4 chars in sequence
print(letters[-4:])
print(letters[-1:]) # prints last char
print(letters[:1]) # prints first char


