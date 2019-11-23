# string manipulation
def _sub_string():
    string1 = 'Hello-World'
    string2 = 'Intelligent'

    # first char in string1
    print(string1[0])
    # last char in string2
    print(string2[-1])

    # print 'elli' - collect sub-string
    print(string2[3:-4])
    print(string2[3:7])


# find - finds a char in string and returns its index value
def _find_function():
    string3 = 'attachment'
    return string3.find('n')


# replace - replaces targeted string/char with given string/char
def _replace():
    string4 = 'hello'
    return string4.replace('o', 'oworld')


# split - splits string based on given splitter
def _split():
    string5 = 'word1,word2,word3'
    return string5.split(',')
    # remember that the output will be a list of separate words


# count - gives you count of the char in the string
def _count():
    string6 = 'DataScience'
    return string6.count('a')


# upper - converts lower case chars in the string to upper
def _upper():
    string7 = 'DataScience'
    return string7.upper()


# lower - converts upper case chars in the string to lower
def _lower():
    string7 = 'DataScience'
    return string7.lower()


# max - returns char with max ASCII value in the string
def _max():
    string8 = '!@#123baBaCc'
    return max(string8)


# min - returns char with min ASCII value in the string
def _min():
    string8 = '!@#123baBaCc'
    return min(string8)