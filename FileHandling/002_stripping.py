"""
    strip() method:
        Return a copy of the string with leading and trailing whitespace remove.
        If chars is given and not None, remove characters in chars instead.
"""


def removeprefix(string: str, prefix: str) -> str:
    if string.startswith(prefix):
        return string[len(prefix):]
    else:
        return string[:]


def removesuffix(string: str, suffix: str) -> str:
    if suffix and string.endswith(suffix): # suffix = '' should not call string[:-0]
        return string[:-len(suffix)]
    else:
        return string[:]



filename = 'jabberwocky.txt'
with open(filename) as poem:
    first = poem.readline().rstrip()

print(first)

chars = "'Twas"
no_apostrophe = first.strip(chars)
print(no_apostrophe)

print('*' * 80)

# removeprefix() and removesuffix methods work with Python 3.9 versions or greater.
# twas_removed = first.removeprefix("'Twas")
twas_removed = removeprefix(first, "'Twas")
print(twas_removed)
# toves_removed = first.removesuffix('toves')
toves_removed = removesuffix(first, 'toves')
print(toves_removed)
