def q1(s: str, n: int):
    new_string = s = list(s)
    for i in range(int(n/len(s))):
        s += new_string
    return s[:n].count('a')


print(q1('abcac', 10))
