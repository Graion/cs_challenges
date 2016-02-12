function giveMeChange(coins, change) {
    let coin = coins.slice(-1).shift();
    if (coin) {
        return Math.floor(change / coin) + gimeMeChange(coins.slice(0, -1), change % coin);
    } else {
        return 0;
    }
}

console.log(giveMeChange([1, 5, 10], 28)); // => 6
