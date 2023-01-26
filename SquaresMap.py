def square_num(n):
    return n*n

nums = [4,5,2,9]
print("original List:",nums)
result=map(square_num,nums)
print("square the elements of list using map():")
print(list(result))

