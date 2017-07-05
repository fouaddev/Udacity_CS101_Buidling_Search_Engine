# EXPLORING LIST PROPERTIES

# Investigating adding and appending to lists
# If you run the following four lines of codes, what are list1 and list2?

list1 = [1,2,3,4]
list2 = [1,2,3,4]

list1 = list1 + [5, 6]
list2.append([5, 6])

# The answer is:
list1 = [1,2,3,4,5,6]
list2 = [1,2,3,4,[5,6]]

# to check, you can print them out using the print statements below.

print "showing list1 and list2:"
print list1
print list2

###############################################################################

# SYMMETRIC SQUARE

# A list is symmetric if the first row is the same as the first column,
# the second row is the same as the second column and so on. Write a
# procedure, symmetric, which takes a list as input, and returns the
# boolean True if the list is symmetric and False if it is not.

def transpose(square):
    i = 0
    column_square = []
    for e in square:
        while i < len(e):
            sub_column_square = []
            for e in square:
                sub_column_square.append(e[i])
            column_square.append(sub_column_square)
            i += 1
    return column_square

def symmetric(square):
    if square == transpose(square):
        return True
    return False

print symmetric([[1, 2, 3],
                 [2, 3, 4],
                 [3, 4, 1]])
#>>> True

print symmetric([["cat", "dog", "fish"],
                 ["dog", "dog", "fish"],
                 ["fish", "fish", "cat"]])
#>>> True

print symmetric([["cat", "dog", "fish"],
                 ["dog", "dog", "dog"],
                 ["fish","fish","cat"]])
#>>> False

print symmetric([[1, 2],
                 [2, 1]])
#>>> True

print symmetric([[1, 2, 3, 4],
                 [2, 3, 4, 5],
                 [3, 4, 5, 6]])
#>>> False

print symmetric([[1,2,3],
                  [2,3,1]])
#>>> False


###############################################################################


# SYMMETRIC SQUARE WITH 1 LINE OF CODE SOLUTION: using map & zip built-in functions

def symmetric(square):
    return square == map(list, zip(*square))


###############################################################################


# MEAN OF A LIST

# The mean of a set of numbers is the sum of the numbers divided by the
# number of numbers. Write a procedure, list_mean, which takes a list of numbers
# as its input and return the mean of the numbers in the list.

# Hint: You will need to work out how to make your division into decimal
# division instead of integer division. You get decimal division if any of
# the numbers involved are decimals.

def list_mean(num_list):
    if num_list == []:
        return "No data given"
    return sum (num_list) / (len(num_list) * 1.0)

print list_mean([1,2,3,4])
#>>> 2.5
print list_mean([1,3,4,5,2])
#>>> 3.0
print list_mean([])
#>>> ??? You decide. If you decide it should give an error, comment
# out the print line above to prevent your code from being graded as
# incorrect.
print list_mean([2])
#>>> 2.0
