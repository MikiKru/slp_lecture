from random import Random

generated_values = set()

# generated_values.add(1)
# generated_values.add(1)
# generated_values.add(1)
# generated_values.add(2)
# print(generated_values)

# loop which will works when the condition will be true
while(len(generated_values) < 6):
    value = Random().randint(1,50)
    generated_values.add(value)
    print(value)
print(generated_values)


A = set([1,"S",3,4,5])
B = set([4,5,6,7])

print(A | B)
print(A & B)
print(A - B)
print(A ^ B)