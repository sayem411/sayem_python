s=set([1,2,3,4])
print(s)
print(type(s))
s.add('a')
print(s)
fs=frozenset([1,2,3,4])
print(fs)

s1=set([1,3,7,2])
s2=set([3,2,8,9])
print(s1.union(s2))
print(s1.intersection(s2))
print(s1.difference(s2))






