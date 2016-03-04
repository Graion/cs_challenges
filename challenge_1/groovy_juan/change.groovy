

def giveMeChange(values, change){
  def numberOfCoins = 0
  values.reverseEach { x ->
    numberOfCoins += change.intdiv(x)
    change = change % x
  }
  return numberOfCoins
}


assert giveMeChange([1, 5, 10], 28) == 6