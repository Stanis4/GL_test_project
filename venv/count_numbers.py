def count_numbers():
   with open("number.TXT", encoding='utf-8') as file:
       sum_count = 0
       lines = file.readlines()
       for line in lines:
           if line.startswith("#"):
               continue
           for item in range(0, len(line)):
               print(line[item])
               if (line[item] == '-') and line[item + 1].isdigit() == True:
                   sum_count -= float(line[item+1])
               elif (line[item-1] != '-') and line[item].isdigit() == True:
                   sum_count += float(line[item])
       return "Summ of numbers in the file is ", sum_count


print(count_numbers())