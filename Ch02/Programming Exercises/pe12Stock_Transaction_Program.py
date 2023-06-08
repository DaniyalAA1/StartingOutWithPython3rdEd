# Joe purchased 2000 shares
# When Joe purchased the stock, he paid $40.00 per share
# Joe paid his stockbroker a commission of 3 percent of the amount 
# he paid for the stock

# Two weeks later, Joe sold the stock
# Joe sold 2000 shares
# he sold the stock for $42.75 per share
# He paid his stockbroker another commission that amounted to 3 percent
# of the amount he received for the stock

# Write a program that displays the following informnation
# 1. The amount of money Joe paid for the stock
# 2. The amount of commission Joe paid hsi broker when he bought the stock
# 3. The amount Joe sold the stock for
# 4. The amnount of commission Joe paid his broker when he sold the stock
# Display the amount of money that Joe had left when he sold the stock
# and paid his broker (both times). 
# If this amount is positive, then Joe made a profit
# If the amount is negative, Joe lost money

numberOfShares = 2000
purchasedSharePrice = 40
initialMoneyPaidForStock = numberOfShares * purchasedSharePrice # 80000
initialBrokerCommission = 0.03 * initialMoneyPaidForStock # 2400

sharesSold = 2000
soldSharePrice = 42.75
moneyAfterSelling = sharesSold * soldSharePrice # 85500
secondBrokerCommission = 0.03 * moneyAfterSelling # 2565
totalBrokerCommission = initialBrokerCommission + secondBrokerCommission # 4965
moneyMadeAfterSaleOfStock = moneyAfterSelling - initialMoneyPaidForStock # 5500
profit = moneyMadeAfterSaleOfStock - totalBrokerCommission # 535





print('Joe initially paid',initialMoneyPaidForStock, 'dollars for the stock')
print('Joe paid his broker a commission for buying this stock,\n and the commission was', initialBrokerCommission,'dollars')
print('After two weeks, Joe sold the stock for', moneyAfterSelling,'dollars')
print('Joe paid his broker a commission for selling the stock, which was', secondBrokerCommission,'dollars')
print('After Joe sold the stock, and after he paid his broker both times,\nhe made a profit of', profit,'dollars')
