def calc_sum(a,b):
    sum = a+b
    print(sum)
    return sum
calc_sum(5,10)
calc_sum(2,10)
calc_sum(12,17)
def calc_sum(a,b):
    return a+b
sum = calc_sum(2,10)
print(sum)

#average of 3 numbers
def calc_avg(a,b,c):
    sum = a+b+c
    avg = sum/3
    print(avg)
    return avg
calc_avg(1,2,3)



cities = ["delhi","gurgaon","noida","pune","mumbai"]
def print_len(list):
    print(len(list))
print_len(cities)


heroes =["thor","ironman","captain america"]
def print_list(list):
    for item in list:
        print(item,end="")
print_list(heroes)


def cal_fact(n):
    fact = 1
    for i in range(1,n+1):
        fact *=i
    print(fact)    

    

