#The provided code stub reads two integers from STDIN,  and . Add code to print three lines where:

#The first line contains the sum of the two numbers.
#The second line contains the difference of the two numbers (first - second).
#The third line contains the product of the two numbers.

#Input Format

#The first line contains the first integer, .
#The second line contains the second integer, .

#Sample Input 0

#3
#2

#Sample Output 0

#5
#1
#6
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a+b)
    print(a-b)
    print(a*b)