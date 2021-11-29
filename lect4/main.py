from lect4.functions import generateRandomIntegerFromInterval, divideSentenceIntoWords, generateRandomBoolean, \
    calculateAvgFromGrades, calculateAvgFromGradesNamed

print(generateRandomIntegerFromInterval(10, 4, 10))
print(generateRandomIntegerFromInterval(5, 0, 5))
print(divideSentenceIntoWords("to be, or not to be!"))
generateRandomBoolean()
generateRandomBoolean()
generateRandomBoolean()
print(generateRandomIntegerFromInterval(length=5, top_treshold=6))
print(generateRandomIntegerFromInterval(top_treshold=6, length=10, low_tres= 1))

grades_avg1 = calculateAvgFromGrades(5,4,4.5,3,5,5,5,3)
grades_avg2 = calculateAvgFromGrades(3,5,5,5,3)
grades_avg3 = calculateAvgFromGrades()
print(f"student: X, subject SLP, avg: {grades_avg1}")
print(f"student: Y, subject OOP, avg: {grades_avg2}")
print(f"student: Z, subject IT, avg: {grades_avg3}")
print("DOUBLE STAR")
grades_avgN = calculateAvgFromGradesNamed(lab1=5, lab2=3, lab3=4.5)
print(f"student: Z, subject IT, avg: {grades_avgN}")