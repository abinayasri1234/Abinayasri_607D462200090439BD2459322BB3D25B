class Student:
 
  def __init__(self, name, roll_number, cgpa):
    self.name = name
    self.roll_number = roll_number
    self.cgpa = cgpa


def sort_students(student_list):

  sorted_students = sorted(student_list,
                    key=lambda student: student.cgpa,
                    reverse =True)
  return sorted_students



students = [
    Student("Abi","A123",7.8),
    Student("Rock","A124",9.8),
    Student("Bby","A125",6.9),
    Student("Aruva","A126",9.8),
]

sorted_students = sort_students(students)

for student in sorted_students:
  print("Name: {}, Roll Number: {}, CGPA: {}".format(student.name,
                                       student.roll_number,
                        student.cgpa))
  