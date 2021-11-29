from random import randint, choice


# functions
# function that returns the random numbers from specified interval
def generateRandomIntegerFromInterval(length, low_tres = 0, top_treshold = 100):
    random_values = []
    for sample in range(1, length + 1):
        random_values.append(randint(low_tres, top_treshold))
    return random_values

def divideSentenceIntoWords(sentence):
    clean_sentence = ""
    for character in sentence:
        if character.isalnum() or character == ' ':
            clean_sentence += character
    return clean_sentence.split()

def generateRandomBoolean():
    random_boolean = choice([True, False])
    print(f"Random boolean: {random_boolean}")

def calculateAvgFromGrades(*grades):
    if len(grades) == 0:
        return "N/C"
    sum = 0
    for index, grade in enumerate(grades):
        print(index, grade)
        sum += grade
    return round(sum/len(grades), 2)

def calculateAvgFromGradesNamed(**grades):
    if len(grades) == 0:
        return "N/C"
    sum = 0
    for key, grade in grades.items():
        print(key, grade)
        sum += grade
    return round(sum/len(grades), 2)
