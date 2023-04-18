'''
Input = 5
Output =      *
             ***
            *****
           *******
          *********
'''
Number = int(input("Fill number : "))
for i in range(Number):
    i = i+1
    print(" "*(Number-i), "*"*((2*i)-1))
  