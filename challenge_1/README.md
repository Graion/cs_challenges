# Coins

You're given a list of coin values `[V1, V2, ..., VN]` and a required change `C`.

Your task is to write an algorithm that prints to the standard output (`stdout`) the minimum number of coins required to give the change `C`.

## Notes

* The coins are sorted in ascending order by their value.
* It is guaranteed that the change can be obtained (i.e. there won't be any tests like `V: [10, 50], C: 75`).
* Expected complexity: `O(C * N)`.

## Example

Input: `V = [1, 5, 10], C = 28`
Output: `6`
Explanation: `1 + 1 + 1 + 5 + 10 + 10 = 28`
