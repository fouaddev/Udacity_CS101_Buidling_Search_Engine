# BETTER HASH FUNCTION

# Define a function, hash_string,
# that takes as inputs a keyword
# (string) and a number of buckets,
# and returns a number representing
# the bucket for that keyword.

def hash_string(keyword,buckets):
    return sum(ord(i) for i in keyword) % buckets

print hash_string('a',12)
#>>> 1

print hash_string('b',12)
#>>> 2

print hash_string('a',13)
#>>> 6

print hash_string('au',12)
#>>> 10

print hash_string('udacity',12)
#>>> 11

------------------------------------------------------------------------------

# EMPTY HASH TABLE

# Creating an Empty Hash Table
# Define a procedure, make_hashtable,
# that takes as input a number, nbuckets,
# and returns an empty hash table with
# nbuckets empty buckets.

def make_hashtable(nbuckets):
    hash_table = []
    for i in range(0, nbuckets):
        hash_table.append([])
    return hash_table
    
print make_hashtable(3)
#>>> [[], [], []]

------------------------------------------------------------------------------

# FINDING BUCKETS

# # Define a procedure, hashtable_get_bucket,
# that takes two inputs - a hashtable, and
# a keyword, and returns the bucket where the
# keyword could occur.

def hashtable_get_bucket(htable,keyword):
    return htable[hash_string(keyword, len(htable))]

def hash_string(keyword,buckets):
    out = 0
    for s in keyword:
        out = (out + ord(s)) % buckets
    return out

def make_hashtable(nbuckets):
    table = []
    for unused in range(0,nbuckets):
        table.append([])
    return table


table = [[['Francis', 13], ['Ellis', 11]], [], [['Bill', 17],
['Zoe', 14]], [['Coach', 4]], [['Louis', 29], ['Rochelle', 4], ['Nick', 2]]]

print hashtable_get_bucket(table, "Zoe")
#>>> [['Bill', 17], ['Zoe', 14]]

print hashtable_get_bucket(table, "Brick")
#>>> []

print hashtable_get_bucket(table, "Lilith")
#>>> [['Louis', 29], ['Rochelle', 4], ['Nick', 2]]

------------------------------------------------------------------------------

# ADDING KEYWORDS

# # Define a procedure,
#
#    hashtable_add(htable,key,value)
#
# that adds the key to the hashtable (in 
# the correct bucket), with the correct 
# value and returns the new hashtable.
#
# (Note that the video question and answer
#  do not return the hashtable, but your code
#  should do this to pass the test cases.)

def hashtable_add(htable,keyword,value):
    hashtable_get_bucket(htable, keyword).append([keyword, value])
    return htable 

def hashtable_get_bucket(htable,keyword):
    return htable[hash_string(keyword,len(htable))]

def hash_string(keyword,buckets):
    out = 0
    for s in keyword:
        out = (out + ord(s)) % buckets
    return out

def make_hashtable(nbuckets):
    table = []
    for unused in range(0,nbuckets):
        table.append([])
    return table

table = make_hashtable(5)
hashtable_add(table,'Bill', 17)
hashtable_add(table,'Coach', 4)
hashtable_add(table,'Ellis', 11)
hashtable_add(table,'Francis', 13)
hashtable_add(table,'Louis', 29)
hashtable_add(table,'Nick', 2)
hashtable_add(table,'Rochelle', 4)
hashtable_add(table,'Zoe', 14)
print table
#>>> [[['Ellis', 11], ['Francis', 13]], [], [['Bill', 17], ['Zoe', 14]], 
#>>> [['Coach', 4]], [['Louis', 29], ['Nick', 2], ['Rochelle', 4]]]

-------------------------------------------------------------------------------

# 
