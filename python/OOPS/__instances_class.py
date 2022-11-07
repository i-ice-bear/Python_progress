"""
    :return: OOPS class having a feature to assign a variable, instance
             for multiple variables, to share a particular object from
             a class,

    :parameter: By default, if a variable is equal to any variable then
                only the parameters will assign to that variable they,
                didn't share to another variable, Like. Local variables
"""


class Students_along_subjects:
    """
    :return: Added some objects to the class, for sharing that objects
             to the multiple variables.
    """
    subject_english = ["Yash", "Anshu"]
    subject_science = "Goldy"
    student_leaves = 10


class Student_marks_along_subjects:
    subject_english_a_grade = ["Anshu"]
    subject_english_c_grade = ["Yash"]
    subject_science_f_grade = ["Goldy"]


"""
:return: Equalised some variables to the class.

"""
student_names = Students_along_subjects()
anshu = Students_along_subjects()
yash = Students_along_subjects()
goldy = Students_along_subjects()

print(Students_along_subjects.subject_english)
print(Students_along_subjects.subject_science)
print(Students_along_subjects.student_leaves)
print(Student_marks_along_subjects.subject_english_a_grade)
print(Student_marks_along_subjects.subject_english_c_grade)
print(Student_marks_along_subjects.subject_science_f_grade)
