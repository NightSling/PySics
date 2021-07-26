# The provided code stub reads and integer, n, from STDIN. For all non-negative integers i < n, print i^2.

# Example 1:
# The list of non-negative integers that are less than  is . Print the square of each number on a separate line.
# Input:
# n = 3
# Output:
# 0
# 1
# 4

if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        print(i**2)
