# optimal solution
def large_odd_num(s):
    ind = -1
    for i in range(len(s)-1,-1,-1):
        if (int(s[i]) % 2) == 1:
            ind = i
            break
    i = 0
    while i<=ind and s[i] == '0':
        i += 1
    return s[i:ind+1]
s = "054376"
print(large_odd_num(s))