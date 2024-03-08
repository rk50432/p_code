def bubblesort(arr):
    for i in range(1,len(arr)):
        for j in range(0,len(arr)-i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr
print(bubblesort([9,6,3,17,5]))

from timeit import default_timer as timer

# list
start = timer()
for x in range(100):
    j=[]
    for i in range(10000): j.append(i**2)
end =timer()
print(end-start)

# list comprehensions
start = timer()
for x in range(100):
    j=[i**2 for i in  range(10000)]
end =timer()
print (end -start)

