""" Sorry, the code does not deal with negative numbers"""

def count_numbers():
   with open("number.TXT", encoding='utf-8') as file:
       sum_count = 0
       lines = file.readlines()
       for line in lines:
           if line.startswith("#"):
               continue
           for item in line:
               if item.isdigit() == True:
                   sum_count += float(item)
       return "Summ of numbers in the file is ", sum_count


print(count_numbers())