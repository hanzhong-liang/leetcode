import collections

def taskSolving(tasks):
    N=len(tasks)
    ans=0
    used = collections.defaultdict(int)
    tasks.sort(key=lambda x:x[1])
    for i in range(N):
        k=0
        for j in range(tasks[i][0],tasks[i][1]+1):
            if used[j]:
                k+=1
        if k<tasks[i][2]:
            for j in range(tasks[i][1],tasks[i][0]-1,-1):
                if not used[j]:
                    used[j]=1
                    k+=1
                    ans+=1
                    if k==tasks[i][2]:
                        break
    return ans


tasks = [[1,3,2],[2,5,3],[5,6,2]]
tasks = [[1,4,2],[4,6,2],[8,9,2],[3,5,2]]
tasks = [[]]

print(taskSolving(tasks))