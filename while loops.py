i = 1
while i<= 5:
    print(i)
    i+=1

# print numbers from 1 to 100
i =1
while i<=100:
    print(i)
    i+=1
#multiplication table of a number n
i = 1
while i <=10:
    print(3*i)
    i+=1


#elements of the list
[1,4,9,16,25,36,49,64,81,100]
nums = [1,4,9,16,25,36,49,64,81,100]
idx = 0
while idx < len(nums):
    print(nums[idx])
    idx +=1


#tuple using loop
{1,4,9,16,25,36,49,64,81,100}
nums = {1,4,9,16,25,36,49,64,81,100}
x = 36
i = 0
while i<len(nums):
    if(nums[i]==x):
        print("FOUND at idx = 1")


#Break & continue
i = 1
while i<=5:
    print(i)
    if(i==3):
        break
    i+=1
print("end of loop")




i = 0
while i<=5:
    if(i==3):
        i+=1
        continue
    print(i)
    i+=1