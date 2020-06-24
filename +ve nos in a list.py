l = [] 
n = int(input("Enter number of elements:"))
for i in range(0, n): 
    ele = int(input()) 
    l.append(ele)
for num in l: 
      if num >= 0: 
       print(num, end = " ") 
