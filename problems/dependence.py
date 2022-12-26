def func(services):
    linkList = []
    def dfs(index, link):
        if services[index] == -1:
            linkList.append(link)
        dfs(index, link.append(services[index]))
    
    