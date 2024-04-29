import time

print(time.gmtime(0))

# print(time.localtime(time.time()))

# print(time.time()) # prints the no. of seconds passed since epoch (Jan 1, 1970)

time_here = time.localtime() # returns the named tuple
print(time_here)
print("Year:", time_here[0], time_here.tm_year)
print("Month:", time_here[1], time_here.tm_mon)
print("Day:", time_here[2], time_here.tm_mday)
