import math

def main():
    math_grade = int(input("Math grade: "))
    english_grade = int(input("English grade: "))
    global_st_grade = int(input("Gloabal Studies grade: "))
    art_grade = int(input("Art grade: "))

    grades = {"English" : english_grade,
              "Math" : math_grade,
              "Global Studies" : global_st_grade,
              "Art" : art_grade}
    
    
    average_grade = sum(grades.values()) / len(grades)

    print(grades)
    print("Your average grade is a ", average_grade)

    changed_subject = input("Change grade for which subject? ")
    new_grade = int(input("Grade for " + changed_subject + " ?" ))
    grades[changed_subject] = new_grade

    average_grade = sum(grades.values()) / len(grades)

    print(grades)
    print("Your average grade is a ", average_grade)






 
main()