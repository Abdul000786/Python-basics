#!/usr/bin/env python
# coding: utf-8

# ##Question no.1
# 
# The feature responsible for generating Regex objects is the re module in Python. You can import this module to work with regular expressions

# ##Question no.2
# 
# Raw strings (prefixed with r) are often used in Regex objects to avoid escaping special characters. In regular expressions, backslashes (\) are used to escape special characters, but in raw strings, they are treated as literal characters. Since regular expressions often contain backslashes to represent special characters, using raw strings helps avoid double escaping and makes the patterns more readable

# ##Question no.3
# 
# The search() method of a Regex object returns a Match object if the pattern is found in the searched string. If no match is found, it returns None.

# ##Question no.4
# 
# From a Match object, you can get the actual strings that match the pattern using the group() method. Calling group() without any arguments returns the entire matched string. You can also use group(n) to get the string that matches the specified capture group, where n is the group number.

# ##Question no.5
# 
# In the regex created from r'(\d\d\d)-(\d\d\d-\d\d\d\d)', Group 0 covers the entire matched string. Group 1 covers the first set of three digits before the hyphen, and Group 2 covers the second set of three digits after the hyphen.

# ##Question no.6
# 
# In standard expression syntax, to match real parentheses and periods, you can escape them with a backslash (\). For example, to match a literal opening parenthesis, you would use \(, and to match a literal period, you would use \.

# ##Question no.7
# 
# The findall() method returns a list of all non-overlapping matches of the pattern in the searched string. If the pattern contains capturing groups, it returns a list of tuples where each tuple represents a match and contains the captured groups. If the pattern has no capturing groups, it returns a list of strings.

# ##Question no.8
# 
# In standard expressions, the | character acts as the OR operator. It is used to match either the expression on its left or the expression on its right. For example, A|B will match either 'A' or 'B'.

# ##Question no.9
# 
# In regular expressions, the . character (dot) represents any character except a newline. It is used to match any single character except for a newline character

# ##Question no.10
# 
# In regular expressions, the + character is a quantifier that matches one or more occurrences of the preceding element. It requires at least one occurrence of the element. On the other hand, the * character is also a quantifier but matches zero or more occurrences of the preceding element. It allows for zero occurrences of the element.

# ##Question no.11
# 
# In regular expressions, {4} specifies an exact repetition of the preceding element four times. It matches exactly four occurrences. {4,5} specifies a range of repetitions, matching the preceding element between four and five times, inclusive.

# ##Question no.12
# 
# In regular expressions, the shorthand character class \d matches any digit (0-9). The shorthand character class \w matches any alphanumeric character (letter, digit, or underscore). The shorthand character class \s matches any whitespace character (space, tab, newline).

# ##Question no.13
# 
# In regular expressions, the shorthand character class \D matches any non-digit character. The shorthand character class \W matches any non-alphanumeric character. The shorthand character class \S matches any non-whitespace character.

# ##Question no.14
# 
# The difference between .*? and .* is in their matching behavior. .*? is a non-greedy match and will match as few characters as possible. .* is a greedy match and will match as many characters as possible. The ? after .* makes it non-greedy.

# ##Question no.15
# 
# To match both numbers and lowercase letters, you can use a character class. The syntax for a character class is [...], where you can specify the allowed characters. To match numbers and lowercase letters, you can use [0-9a-z]

# ##Question no.16
# 
# To make a normal expression in regex case-insensitive, you can pass the re.IGNORECASE or re.I flag as the second argument to re.compile(). For example, regex = re.compile(pattern, re.IGNORECASE)

# ##Question no. 17
# 
# In regular expressions, the . character normally matches any character except a newline. However, if the re.DOTALL flag is passed as the second argument to re.compile(), the . character will match any character including a newline

# In[23]:


##Question no.18

import re

numRegex = re.compile(r'\d+')
result = numRegex.sub('X', '11 drummers, 10 pipers, five rings, 4 hen')
print(result)


# ##Question no.19
# 
# Passing re.VERBOSE as the second argument to re.compile() allows you to use verbose mode in regular expressions. It allows you to write more readable and well-structured regex patterns by ignoring whitespace and adding comments within the pattern.

# In[24]:


##Question no.20

import re

pattern = r'^\d{1,3}(,\d{3})*$'

test_cases = ['42', '1,234', '6,368,745', '12,34,567', '1234']

for test_case in test_cases:
    if re.match(pattern, test_case):
        print(f"'{test_case}' is a match")
    else:
        print(f"'{test_case}' is not a match")


# In[25]:


##Question no.21

import re

pattern = r'^[A-Z][a-zA-Z]* Watanabe$'

test_cases = ['Haruto Watanabe', 'Alice Watanabe', 'RoboCop Watanabe',
              'haruto Watanabe', 'Mr. Watanabe', 'Watanabe', 'Haruto watanabe']

for test_case in test_cases:
    if re.match(pattern, test_case):
        print(f"'{test_case}' is a match")
    else:
        print(f"'{test_case}' is not a match")


# In[26]:


##Question no.22

import re

pattern = r'^(Alice|Bob|Carol) (eats|pets|throws) (apples|cats|baseballs)\.$'

test_cases = ['Alice eats apples.', 'Bob pets cats.', 'Carol throws baseballs.',
              'Alice throws Apples.', 'BOB EATS CATS.', 'RoboCop eats apples.',
              'ALICE THROWS FOOTBALLS.', 'Carol eats 7 cats.']

for test_case in test_cases:
    if re.match(pattern, test_case, re.IGNORECASE):
        print(f"'{test_case}' is a match")
    else:
        print(f"'{test_case}' is not a match")


# In[ ]:




