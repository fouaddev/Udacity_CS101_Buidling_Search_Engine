# ADD TO INDEX

# Define a procedure, add_to_index,
# that takes 3 inputs:

# - an index: [[<keyword>,[<url>,...]],...]
# - a keyword: String
# - a url: String

# If the keyword is already
# in the index, add the url
# to the list of urls associated
# with that keyword.

# If the keyword is not in the index,
# add an entry to the index: [keyword,[url]]

index = []

def add_to_index(index,keyword,url):    #create a procedure that adds new keywords and/or url's to index
    for e in index:    #loop over all index lists to see if the input keyword already exist
        if keyword == e[0]:    #test input keyword against first element of each list to see if they match
            e[1].append(url)    #if above argument is true, we append url associated with input keyword to url list
            return    #and then we return result, otherwise we account for the case where there is no keyword match. If we don't return, the next line will be executed by adding a new list with that already existed keyword with its url's, even if we found a match keyword
    index.append([keyword, [url]])    #if keyword doesn't match any keyword in all index lists, then we append a new list that consist of this new keyword and its url
    
add_to_index(index,'udacity','http://udemy.com')
add_to_index(index,'computing','http://acm.org')
add_to_index(index,'udacity','http://npr.org')

print index
#>>> [['udacity', ['http://udacity.com', 'http://npr.org']], 
#>>> ['computing', ['http://acm.org']]]


#######################################################################


# LOOKUP

# Define a procedure, lookup,
# that takes two inputs:

# - an index
# - keyword

# The procedure should return a list
# of the urls associated
# with the keyword. If the keyword
# is not in the index, the procedure
# should return an empty list.

index = [['udacity', ['http://udacity.com', 'http://npr.org']],
         ['computing', ['http://acm.org']]]

def lookup(index,keyword):
    for entry in index:
        if keyword == entry[0]:
            return entry[1]
    return []

print lookup(index,'udacity')
#>>> ['http://udacity.com','http://npr.org']


#####################################################################


# Building The Web Index

