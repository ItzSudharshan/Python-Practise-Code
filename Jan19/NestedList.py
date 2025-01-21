'''
Nsted List 
HackerRank @ https://www.hackerrank.com/challenges/nested-list/problem?isFullScreen=true
'''
li = []
n = int(input())
for i in range(n):
    name = input()
    score = float(input())
    li.append([name, score])
    
scores = []
for name, score in li:
    scores.append(score)

scores = list(set(scores))
scores.sort()

nameli = []
second_smallest_element = scores[1]
for name , score in li:
    if score == second_smallest_element:
        nameli.append(name)

nameli.sort()
for name in nameli:
    print(name)