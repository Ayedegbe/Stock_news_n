student_heights = input("Input a list of student heights ").split(",")
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
total_height = 0
for heights in student_heights:
  total_height += heights
print (f' The total height is {total_height}')
student_number = 0
for number in student_heights:
  student_number += 1
print(f' The total student number is {student_number}')

average = round(total_height/student_number)
print(f' The average height is {average}')
