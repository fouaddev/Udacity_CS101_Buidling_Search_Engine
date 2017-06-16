#Problem Solving for Intro to Computer Science

#Here are a couple of practice problems for you. Try to use Polya's four
#principles as you solve the problems.



# Define a procedure, sum_evens, that takes
# as an argument a list of numbers, and returns
# the sum of all the even integers from the list
# For example,
# sum_evens([1, 2, 3, 4, 5]) = 6
# sum_evens([7, 21, -9]) = 0
# sum_evens([0.5, 4]) = 4

# Define a procedure, how_long_til_lunch, that takes
# three inputs: an integer representing the current hour,
# an integer representing the current minutes, and
# a string that is either 'am' or 'pm'.
# The output should be how long you have to wait from the
# given time until 11:45 am, in minutes (an integer).
# If you're unsure how the 12-hour clock works, see
# http://en.wikipedia.org/wiki/12-hour_clock
# For example, how_long_til_lunch(5, 45, 'pm') = 1080

# Define a procedure, string_split, that takes
# as an argument a list of strings, and returns
# a list of two elements: the first element is the
Copyright © 2014 Udacity, Inc. All Rights Reserved.
# concatenation of all the strings in the first half
# of the list, and the second element is the
# concatenation of all the strings in the second half
# of the list. If the input list is odd length, add the
# middle string to the first element.
# For example,
# string_split(['Hello', ' world!',
# 'Goodnight', ' moon!']) =
# ['Hello world!', 'Goodnight moon!']
# string_split(['one', 'two', 'three']) =
# ['onetwo', 'three']
# string_split([]) = ['', '']
Copyright © 2014 Udacity, Inc. All Rights Reserved.

def string_split(strings_list):
    two_elements_list = [] # introducing an output list that will contain the two list elements
    first_element = ''
    second_element = ''
    if len(strings_list)%2 == 0:
        for e in strings_list[:len(strings_list)/2]:
            first_element = first_element + e
        two_elements_list.append(first_element)
        for e in strings_list[len(strings_list)/2:]:
            second_element = second_element + e
        two_elements_list.append(second_element)
    else:
        for e in strings_list[:(len(strings_list)/2)+1]:
            first_element = first_element + e
        two_elements_list.append(first_element)
        for e in strings_list[(len(strings_list)/2)+1:]:
            second_element = second_element + e
        two_elements_list.append(second_element)
    return two_elements_list
    
print string_split(['Hello', ' world!', 'Goodnight', ' moon!'])
# ['Hello world!', 'Goodnight moon!']

print string_split(['one', 'two', 'three'])
# ['onetwo', 'three']

print string_split([])
# = ['', '']
