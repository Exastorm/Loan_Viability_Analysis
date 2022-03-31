


# def f(x,y,z):
#     return x+y+z

# a=1
# b=2
# c=3

# v=f(a,b,c)

# print(v)


cap=0

def calculate_market_cap(market_price, number_of_shares):
    global cap
    cap = market_price * number_of_shares
    return cap

price = 257
shares = 5000
calculate_market_cap(price, shares)

print(cap)

# def count():
#     global x 
#     x = 88

# lst = list(range(0, 100 +1))
# i = 0
# count()
# while i < x:
#     i = i+1
#     print(i)
    


    