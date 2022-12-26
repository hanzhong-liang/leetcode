def shortestPathLength(graph):
    n = len(graph)
    frontier = []
    temp = [0] * n
    for i in range(n):
        temp[i] = 1
        # 其实这个temp和1<<i表示的是完全相同的状态
        frontier.append((i, tuple(temp)))
        temp[i] = 0
    # 必须是tuple因为list是属于unhashable的
    explored = set(frontier)
    goal = tuple([1] * n)
    step = 0
    while frontier:
        nxt = []
        for cur, state in frontier:
            if state == goal:
                return step
            for other in graph[cur]:
                # 把一个tuple再转换成list，实际上也进行了复制
                temp = list(state)
                # 这就相当于 1 << other | state
                temp[other] = 1
                # 将list转换成tuple，这样可以hash判断有没有走过
                successor = (other, tuple(temp))
                if successor not in explored:
                    explored.add(successor)
                    nxt.append(successor)
        frontier = nxt
        step += 1
    # 图不连通
    return -1


graph = [[]]
shortestPathLength(graph)