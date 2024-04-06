"""
    Whitespace: 
        Whitespace is any character that represents horizontal or vertical spacing.
        Whitespace characters aren't visible as characters, but they do space things out.
        Ex: space, tab, newline
    str.strip(): Return a copy of the string with leading and trailing whitespace removed
"""
jabber = open('jabberwocky.txt', 'r')

for line in jabber:
    # print(line, end='')  # to removing '\n' char from each line
    print(line.strip())  # strip off the '\n' char from end of line

jabber.close()
