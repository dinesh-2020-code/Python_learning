"""
Hashing Functions
    -> A hash function produces fixed-size hash values from its input. The hashes are usually integers, but don't
    have to be,
    -> There are many different ways to implement a hash function. There's no single way to write one, and different
    algorithms have their own strengths, weaknesses and applications.
    -> A hash function produces values that can be used to index a fixed-size data structure, called a `hash table`.
    If the hash table hold 500 items, then the hash function should produce 500 distinct hashes.
    -> There are several different strategies for handling collisions. One of the simplest, is to dump all keys with
    the same hash into the same "bucket". You then compare each item in the bucket with the original key, to see
    if exists.
    -> Because handling collisions is slower than indexing directly into the table, it's important that a hash
    function produces as few collisions as possible.
    -> The best case is that every key has a unique hash.
    -> The worst case is that every key has the same hash - if that happens, the hashing function isn't suitable for
    that particular application.

ASCII and Python built-in hash() function
    -> Every char is represented by a number, when it's stored in the computer. In the very early days of computing,
    that used to be the ASCII value (ASCII: American Standard Code for Information Interchange). 
    -> These days, we don't use ASCII, we use `Unicode`. ASCII can only represent 127 different chars. That's not
    enough to handle all the languages and character sets, that are used throughout the world.
    
    Python's hash() function
        -> Python hash() randomizes the hashes that it produces. You'll get the same hash for any particular string,
        while your programs's running. But each time you run the program, the hash codes will be different.
        -> That was introduced in Python 3.3, to prevent Denial of Service(DoS) attacks on web servers using Python 
        dictionaries. 
        
    -> If different keys can produce the same hash, then it should be obvious that you can't get the key back from its
    hash. You can't reverse the process to find out a value from its hash.

"""