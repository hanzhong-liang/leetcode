# x=[4,6,4,-4,1]
# y=[-1,1,-5,-4,5]

x=[1,5]
y=[1,5]

# x=[1,4]
# y=[1,4]

N=len(x)
y.sort()
x.sort()

l,r=0,N-1
cost_y = 0
cost_x = float('INF')

while l<r:
    cost_y += y[r] -y[l]
    r-=1
    l+=1

x_temp_cost = 0
for i in range(-1,2):
    mid = N//2 
    center = x[mid]+i
    while mid<N:
        x_temp_cost+=abs(x[mid]-center)
        mid+=1
        center+=1

    mid = N//2
    center = x[mid]+i-1
    mid-=1
    while mid>-1:
        x_temp_cost+=abs(x[mid]-center)
        mid-=1
        center-=1
    cost_x = min(cost_x, x_temp_cost)

print(cost_x)
print(cost_y)

