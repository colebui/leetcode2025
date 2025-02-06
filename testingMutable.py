variable1 = "hello"
variable2 = variable1
variable2 = "world"

print(variable1)  # Outputs: hello

print(variable2)  # Outputs: world

list1 = [1,2,3]
list2 = list1
list2.append(4)

print(list1)  # Outputs: [1, 2, 3, 4]

print(list2)  # Outputs: [1, 2, 3, 4]]

original = [1, 2, 3]
shallow_copy = original[:]
shallow_copy[0] = 99
print(original)