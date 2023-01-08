def last(n):
    return n[-1]
def sort(a):
    return sorted(a,key=last)

a=[(2,5),(1,2),(4,4),(2,3),(2,1)]
print("sorted:")
print(sort(a))
