class Student:
    amount_of_student = 0
    print("Hi")

        def __init__(self, name=None, scholarship=50):
            self.name = name
            self.height = 170
            print("I am alive!")
            Student.amount_of_student += 1
            self.scholarship = scholarship

        def __str__(self):
            return f"I am a Student. My name is {self.name}"

        def add_scholarship(self):
            self.scholarship += 106

        def __del__(self):
            print(f"The student {self.name} is no longer enrolled at the university.")
            Student.amount_of_student -= 1

    print("-" * 18, "Tom", "-" * 18, sep="")
    tom = Student(name="Tom", scholarship=100)
    tom.add_scholarship()
    print(tom.amount_of_student)
    print(f"Scholarship Tom: {tom.scholarship}")
    print(tom)

    print("-" * 16, "Bill", "-" * 10, sep="")
    bill = Student(name="Bill")
    bill.add_scholarship()
    bill.add_scholarship()
    print(bill.amount_of_student)
    print(f"Scholarship Bill: {bill.scholarship}")
