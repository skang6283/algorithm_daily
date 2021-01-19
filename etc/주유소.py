num_cities=int(input())
dist=[int(x) for x in input().split()]
price=[int(x) for x in input().split()]

current_min = price[0]
min_price=[0]*num_cities
min_price[0] = current_min*dist[0]
for i in range(1,num_cities-1):
    if price[i] < current_min:
        current_min = price[i]

    min_price[i]= min_price[i-1]+ current_min * dist[i]

print(min_price[num_cities-2])
