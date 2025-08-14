def count_up(limit):
    n =0
    while n < limit :
        yield n
        n += 1

for number in count_up(5):
    print(number) 


"""
0
1
2
3
4
"""