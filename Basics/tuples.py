'''
    Tuples
    A tuple is a mathematical name for an ordered set of data
    Tuples are immutable, like strings and unlike lists

    Because they don't have the overhead of the methods needed to change them, tuples use less memory
    than lists. 

    Reasons for preferring a tuple over a list. Both reasons are due to tuples being immutable
        -> to protect the integrity of your data
        -> Always unpack tuples successfully, because a tuples can't be changed, you always know
            how many items to unpack.

'''
# parenthesis is optional while declaring, but parenthesis must be used when passing
# tuple as an argument to function
# t = "a", "b", "c"  # same as t = ("a", "b", "c")
# print(t)
# print(type(t))

# welcome = "Welcome  to my Nightmare", "Alice Cooper", 1975
# bad = "Bad company", "Bad Company", 1974
# budgie = "Nightflight", "Budgie", 1981
# imelda = "More Mayhem", "Emilda May", 2011
# metallica = "Ride the lightening", "Metallica", 1984

# print(metallica)
# # access through index
# print(metallica[0])
# print(metallica[1])
# print(metallica[2])

# # tuples are immutable
# # metallica[0] = "master of puppets"  # TypeError: 'tuple' object does not support item assignment

# metallica2 = list(metallica)
# print(metallica2)

# metallica2[0] = "master of puppets"
# print(metallica2)

# a = b = c = d = e = f = 12
# print(c)

# # tuple unpacking
# x, y = 1, 2
# print(x, type(x))
# print(y, type(y))

# print("unpacking a tuple")
# data = 1, 2, 76
# x, y, z = data
# print(x)
# print(y)
# print(z)

# Practical use of unpacking tuples
# in enumerate() function -> returns tuple containing (index, value)

# for t in enumerate("abcdefgh"):
#     index, character = t
#     print(index, character)
#     # print(t, type(t))

# Nested tuples and list

albums = [("Welcome  to my Nightmare", "Alice Cooper", 1975),
           ("Bad company", "Bad Company", 1974),
           ("More Mayhem", "Emilda May", 2011),
           ("Ride the lightening", "Metallica", 1984),
           ]

for (name, artist, year) in albums:
    print("Album: {}, Artist: {}, Year: {}"
          .format(name, artist, year))