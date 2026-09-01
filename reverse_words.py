# brute force approach
def reverse_words(s):
    words = []
    word = ""
    for ch in s:
        if ch != " ":
            word += ch
        elif word:
            words.append(word)
            word = ""
    if word:
        words.append(word)
    words.reverse()
    return " ".join(words)
s = "hello ram vilas    reddy"
print(reverse_words(s))
# optimal solution
def reverse_word(s):
    result = ""
    i = len(s)-1
    while i>=0:
        while i>=0 and s[i] == " ":
            i -= 1
        if i<0:
            break
        end = i
        while i>=0 and s[i] != " ":
            i -= 1
        word = s[i+1:end+1]
        if result != " ":
            result += " "
        result += word
    return result
s = "hello ram vilas    reddy"
print(reverse_word(s))