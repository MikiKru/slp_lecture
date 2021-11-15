names = ['John', 'Andy', 'Kate', 'Alan']
# foreach
for name in names:
    print(name)

num = 3.1454324242
print(f'number round to 2 places: {num:10.3}')
for index, name in enumerate(names):
    print(f'index {index:2} value {name:10}')

while True:
    decision = input("Are you want to quit the program?")
    if decision.upper() == "Q":
        break