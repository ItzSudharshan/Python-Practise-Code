def mutation(string,position,character):
    li = list(string)
    li[position] = character
    string = "".join(li)
    return string



s = input()
p, c = input().split()
mutation(s,int(p), c)