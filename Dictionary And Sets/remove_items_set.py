small_ints = set(range(21))
print(small_ints)

# small_ints.clear()
# print(small_ints)

# remove() and discard() methods
# discard(): Remove an element from a set if it is a member. If the element is not a member, do nothing
# remove() : Remove an element from a set; it must be a member.If the element is not a member, raise a KeyError.

small_ints.discard(10)  # Ensure that something no longer exists
small_ints.remove(11)   # Remove something if it exists
print(small_ints)

small_ints.discard(21)
print(small_ints)
# small_ints.remove(22)  # KeyError: 22
