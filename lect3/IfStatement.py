# GRADES
# 50% - 60% - 3.0
# 60% - 70% - 3.5
# 70% - 80% - 4.0
# 80% - 90% - 4.5
# 90% - 100% - 5.0

student_result = int(input("How many points did you gain?"))
total_pts = 50
student_result_percent = 100 * (student_result/total_pts)
print(student_result_percent)
if (student_result_percent >= 90):
    print("5.0")
elif(student_result_percent >= 80):
    print("4.5")
elif(student_result_percent >= 70):
    print("4.0")
elif(student_result_percent >= 60):
    print("3.5")
elif(student_result_percent >= 50):
    print("3.0")
else:
    if(student_result_percent == 0):
        print("Not participate!")
    else:
        print("2.0")



