from array imoprt *
arr = array('i', [])

n = int(input("Enter the length of the Array "))

for i in range(n):
    x = int(input("Enter the Values you want in your Array "))
    arr.append(x)
    
print(arr)
