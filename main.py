# def greet(name):
#   print(f"hello {name}")
#   print("how do you do")

# greet("Jack")




# PASSING MULTIPLE ARGUMENTS

# def add_number(n1, n2):
#   result = n1 + n2
#   print(f"the total sum is {result}")

# number1 = 45
# number2 = 45

# add_number(number1,number2)



# RETURNING A VALUE FROM A FUNCTION

def total_number(num1,num2):
  result = num1 + num2
  return result

first_num = 29
second_num =34

sum_total=total_number(first_num,second_num)
print(f"the total number is {sum_total}")


# make  a function 

def avarage_marks(marks):
  total = sum(marks)
  length = len(marks)
  avarage = total/length
  print(avarage)
  return avarage


marks = [23,23,32,80,65]
final = avarage_marks(marks)
if final >= 80:
  print("Your grade is A")
elif final >=60 and final < 80:
  print("Your grade is B")
elif final >= 50 and final < 60:
  print("Your grade is C")
else:
  print("Your grade is F")