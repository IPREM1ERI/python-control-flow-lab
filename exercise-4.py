# exercise-04 What kind of Triangle?

# Write the code that:
# 1. Prompts the user to enter the three lengths of a triangle (one at a time):
#      Enter the lengths of three side of a triangle:
#      a: 
#      b:
#      c:
# 2. Write the code that determines if the triangle is:
#      equalateral - all three sides are equal in length
#      scalene - all three sides are unequal in length
#      isosceles - two sides are the same length
# 3. Print a message such as:
#      - A triangle with sides of <a>, <b> & <c> is a <type of triangle> triangle

length_a = int(input("Enter the lengths of three side of a triangle (side A):"))
length_b = int(input("Enter the lengths of three side of a triangle (side B):"))
length_c = int(input("Enter the lengths of three side of a triangle (side C):"))

triangle = [length_a, length_b, length_c]

countA = triangle.count(length_a)
countB = triangle.count(length_b)
countC = triangle.count(length_c)

total = countA + countB + countC

if total == 9:
  print(f"A triangle with sides of {length_a}, {length_b} & {length_c} is a equalateral triangle")
elif total == 5:
  print(f"A triangle with sides of {length_a}, {length_b} & {length_c} is a isosceles triangle")
else:
  print(f"A triangle with sides of {length_a}, {length_b} & {length_c} is a scalene triangle")