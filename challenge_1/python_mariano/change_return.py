# This is the common, or 'Greedy' solution

def change_gredy(Coins, Change):
  total = 0
  for coin in Coins[::-1]:
    if Coins%coin == 0:
      total += Change/coin
      return total
    else:
      total += Change/coin
      Change = -= (Change/coin) * coin
  print "Total coins used: " + str(total)
V = [1,5,10]
C = 28
change_greedy(V,C)

# This works as long as the change can be returend with subsequent coins.
# So, it works with the case V = [1,3,4] C = 6, because it needs only the 3 coin;
# but won't work with V = [1,4,5,10] C = 28, where 10 and 4 are the requred ones
# and they are not subsequent in the coins array

def change_subsequent(Coins,change):
    minCoinsUsed = "a"
    while len(Coins) > 0:
        total = 0
        rest = change
        for coin in Coins[::-1]:
            if rest%coin == 0:
                total += rest/coin
                rest = 0
                minCoinsUsed = min(total,minCoinsUsed)
            else:
                total += rest/coin
                rest -= (rest/coin) * coin
        print "Starting with " + str(Coins[-1]) + ", used " + str(total) + " coins."
        V.pop()   
        
V = [1,4,5,10]
C = 28

change_subsequent(V,C)

#TODO find a correct solution for the all the cases at the same time
