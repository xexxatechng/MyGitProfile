#Code written by:       Christian Nwachukwu
#Date:                  25/05/2019
#Application puppose:   Application accepts student if the meet requirements.


while True:
    print()
    grade_point_average = eval(input("Enter Grade Point Average: "))
    admission_test_score = eval(input("Enter Test Score: "))
    if(grade_point_average >= 3.0 and (admission_test_score >= 60 and admission_test_score < 80)):
        print("Student Accepted")
    elif(grade_point_average < 3.0 and (admission_test_score>= 80 and admission_test_score <= 100)):
        print("Student Accepted")
    elif(grade_point_average < 0 and admission_test_score > 100):
        print("Student Rejected")
    else:
        print("Invalid")
        print("Press 'y' to re-enter")
        selection = input()
        if selection != 'y':
            break
        else:
            continue
