

def isValid(s):
    parenthesis = []
    for i in s:
        if i == '(' or i == ')':
            parenthesis.append(i)

    if parenthesis[0] == '(':
        return False

    #for p in parenthesis:

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
