# string interpolation
# Python2 had another way of formatting strings, called 'string interpolation.'
# It's useful to understand how it works, but it is not recommended that you use it for any 
# Python3 programs. That's because it's been deprecated, and will be removed from the language
# at some point.

age = 23
print("My age is %d years." % age)

major = "years"
minor = "months"

print("My age is %d %s, %d %s." %(age, major, 6, minor))
print("PI is approximately %f" % (22 / 7))
print("PI is approximately %60.50f" % (22 / 7))
