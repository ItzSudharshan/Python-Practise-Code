'''
Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given  scores. Store them in a list and find the score of the runner-up.

Input Format

The first line contains . The second line contains an array   of  integers each separated by a space.

Constraints

Output Format

Print the runner-up score.

Sample Input 0

5
2 3 6 6 5

Sample Output 0

5
'''
'''
#Finding the Second Largest Element  (Runner Up Score HackerRank)

n = int(input())
li = list(map(int, input().split()))
li = list(set(li))
li.sort(reverse = True)
print(li[1])

'''
#Similar code but find the second smallest element in the array 
n = int(input())
li = list(map(int, input().split()))
li = list(set(li))  # Remove duplicates
li.sort()  # Sort in ascending order
print(li[1])  # Second smallest element
