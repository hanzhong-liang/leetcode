
# 从左边删除一个元素
print(q.popleft()) # a
print(q) # deque(['b', 'c', 'd'], maxlen=10)

# 扩展队列
q.extend(['i', 'j'])
print(q) # deque(['b', 'c', 'd', 'i', 'j'], maxlen=10)

# 查找下标
print(q.index('c')) # 1

# 移除第一个'd'
q.remove('d')
print(q) # deque(['b', 'c', 'i', 'j'], maxlen=10)

# 逆序
q.reverse()
print(q) # deque(['j', 'i', 'c', 'b'], maxlen=10)

# 最大长度
print(q.maxlen) # 10