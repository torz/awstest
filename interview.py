

def isValid(s):
    parenthesis = []
    for i in s:
        if i == '(' or i == ')':
            parenthesis.append(i)

    while len(parenthesis) != 0:

        a = parenthesis.index('(')
        b = parenthesis.index(')')

        if a > b:
            return False

        parenthesis.pop(a)
        parenthesis.pop(b)

    return True

if __name__ == '__main__':
    isValid('(test)')


'''
create a method that returns true/false
check for valid parenthesis
() is valid
()() is valid
(()) is valid
)( is not valid
(( is not valid
)) is not valid
'''
