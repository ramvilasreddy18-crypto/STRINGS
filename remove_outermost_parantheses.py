# remove outermost valid parantheses from the string
def remove(s):
    res = ""
    level = 0
    for char in s:
        if char == '(':
            if level>0:
                res += char
            level += 1
        else:
            level -= 1
            if level>0:
                res += char
    return res
s = "(()())(())"
print(remove(s))