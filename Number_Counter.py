import re

def number_counter(string):
    numbers=re.findall("\d+",string)
    return len(numbers)

string=input("Give me any string and I will count how many numbers it contains\n")
num_count=number_counter(string)
print(num_count)