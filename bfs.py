from collections import deque

graph = [
    [0, 16, 11, 6],
    [8, 0, 13, 16],
    [4, 7, 0, 9],
    [5, 12, 2, 0]
]

city=["A","B","C","D"]
n=len(graph)

queue = deque([(0,[0],0)])
min_cost=999
best_path=[]

while queue:
    current,path,cost=queue.popleft()

    if len(path)==n:
        total=cost+graph[current][0]

        print("Path: ",end=" ")
        for i in path:
            print(city[i],end="->")
        print("A",end=" ")
        print("Cost: ",total)

        if total<min_cost:
            min_cost=total
            best_path=path+[0]
        continue

    for next in range(n):
        if next not in path:
            queue.append((
                next,
                path+[next],
                cost+graph[current][next]
            ))

print("\nOptimal path:","->".join(city[i] for i in best_path))
print("Minimum Cost: ",min_cost)
