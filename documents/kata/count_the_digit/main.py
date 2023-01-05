def nb_dig(n, d):
    total = 0
    for number in range(0, n + 1):
        if str(d) in str(number**2):
            total += str(number).count(str(d))
    return total
    

#or, the ultra elegant one:
#return sum(str(i*i).count(str(d)) for i in range(n+1))
