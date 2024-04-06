"""
    Whitespace: 
        Whitespace is any character that represents horizontal or vertical spacing.
        Whitespace characters aren't visible as characters, but they do space things out.
        Ex: space, tab, newline
    str.strip(): Return a copy of the string with leading and trailing whitespace removed

    File handle:
        File handles(or file descriptors, on Mac and Linux) are used by the Operating system,
        to keep track of the files that have been opened.

        They are system-wide, which means the available file handles are shared by every process
        running on your computer.

        Another consequence of failing to close a file, when writing data to it, is that data
        might be lost. 
        Neither of these situations are good, so it's very important to close every file that you open.

        Python closes the file automatically if we open the file using 'with' statement.
"""
# jabber = open('jabberwocky.txt', 'r')

# for line in jabber:
#     # print(line, end='')  # to removing '\n' char from each line
#     print(line.strip())  # strip off the '\n' char from end of line

# jabber.close()

# with open('jabberwocky.txt', 'r') as jabber:
#     # reading file line by line using for loop
#     # for line in jabber:
#     #     print(line.strip())

#     # readlines() method: returns the list containing the strings for each line
#     lines = jabber.readlines()

# print(lines)
# print(lines[-1])
# for line in reversed(lines):
#     print(line, end='')

# with open('jabberwocky.txt', 'r') as jabber:
#     text = jabber.read()

# # print(text)
# for char in reversed(text):
#     print(char, end='')

with open('jabberwocky.txt') as jabber:  # default mode is 'read' mode
    while True:
        line = jabber.readline().rstrip()
        print(line)
        if 'jubjub' in line.casefold():
            break