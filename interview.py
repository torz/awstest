

def isValid(s):
    parenthesis = []
    for i in s:
        if i == '(' or i == ')':
            parenthesis.append(i)

    while len(parenthesis) != 0:

        try:
            a = parenthesis.index('(')
            b = parenthesis.index(')')
        except:
            return False

        if a > b:
            return False

        parenthesis.pop(a)
        parenthesis.pop(b-1)

    return True

if __name__ == '__main__':
    print(isValid('(test)'))
    print(isValid('((test))'))
    print(isValid('()test()'))
    print(isValid(')test('))
    print(isValid('(test'))


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
