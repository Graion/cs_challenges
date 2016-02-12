def giveMeChange (values, change)
    acc = 0
    values.reverse.each { |x|
        acc += (change / x).floor
        change = change % x
    }
    acc
end

giveMeChange([1, 5, 10], 28) #=> 6
