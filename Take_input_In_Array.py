Python 3.10.5 (tags/v3.10.5:f377153, Jun  6 2022, 16:14:13) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
arr = array('i', [])

n = int(input("Enter the length of the Array "))

for i in range(n):
    x = int(input("Enter the Values you want in your Array "))
    arr.append(x)
    
print(arr)
