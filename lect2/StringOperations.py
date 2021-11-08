language_name = "python"
print(language_name)
# language_name[0] = 'j'
language_name = "jython"
print(language_name)
print(language_name.upper())
print(language_name.capitalize())

# digit_input = input("Write digit")
# if(digit_input.isdigit() and len(digit_input) == 1):
#     print("digit")
#     digit = int(digit_input)
#     print("Ready to convert: ", type(digit))
# else:
#     print("no digit")

# split
sentence = "US rapper Travis Scott is facing legal action after at least eight people were killed and hundreds injured in a crush at his Texas festival Astroworld."
sentence = sentence.lower()
sentence = sentence.replace('.', '')
print(sentence.split(' '))
