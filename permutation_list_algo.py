def perm1(list):
    if len(list) == 0:
        return []
    elif len(list) == 1:
        return [list]
    else:
        l = []
        for i in range(len(list)):
            x = list[i]
            xs = list[:i] + list[i+1:]
            for p in perm1(xs):
                l.append([x]+p)
        return l
data = list('abc')
for p in perm1(data):
    print(p)