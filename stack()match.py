def check(s):
    stack = []                             #(1+2)
    for i in range(len(s)):
        if s[i] == "(":
            stack.append(s[i])

        elif s[i] == ")":
            if not stack:
                return False
            stack.pop()

    if not stack:
        return True
    return False

s = "(1+2))"
print(check(s))            
