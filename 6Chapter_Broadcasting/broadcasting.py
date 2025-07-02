import numpy as np



# problem

# prices = [100, 200, 300]
#
# discount = 10
#
# fPrices = []
#
# for price in prices:
#     fPrice = price - (price * discount/100)
#     fPrices.append(int(fPrice))
#
#
# print(fPrices)


priceArr = np.array([100,200,300])

discount = 10

finalAfterDiscount = priceArr - (priceArr * discount/100)

print(finalAfterDiscount)





