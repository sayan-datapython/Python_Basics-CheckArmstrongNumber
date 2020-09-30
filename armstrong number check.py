# Python program to determine whether the number is
# Armstrong number or not
 


    
       
    
        
    
 


 
   
    
    
       
        

 
# Function to check whether the given number is
# Armstrong number or not
def isArmstrong (n):
    length=len(str(n))
    temp = n
    sum = 0
    while (temp!=0):
        r = temp%10
        sum1 = sum + r**lenght
        temp = temp//10
 
    # If condition satisfies
     if(sum==n):
      print(f'The {n} is an Armstrong number')
     else:
      print(f'The {n} is not an Armstrong number')

    
    
   
   
 
 
# Driver Program
x = 153
print(isArmstrong(x))
x = 1253
print(isArmstrong(x))
