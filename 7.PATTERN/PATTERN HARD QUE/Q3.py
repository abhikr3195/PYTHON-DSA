"""
        1
       222
      33333"""
      
for i in range(1,6):
    for k in range(5-i):
        print("",end=" ")
    for j in range(2*i-1):
        print(i,end="")
    print()