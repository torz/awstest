

def isValid(s):
    parenthesis = 0
    for i in s:
        if i == '(':
            parenthesis += 1
        if i == ')':
            parenthesis -= 1

        if parenthesis < 0:
            return False

    if parenthesis == 0:
        return True
    else:
        return False

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
