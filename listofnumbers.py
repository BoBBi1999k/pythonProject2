from operator import indexOf

numbers = [1,3,4,7,8,9,10,13,21,30]

def sum(list):
    total = 0
    for i in list:
        total = total + i
    return total

def reverse(list):
    reversed_array = []
    for i in list:
        reversed_array.append(list[len(list) - 1 - list.index(i)])
    return reversed_array


print("Total: " + str(sum(numbers)))
print("Reverse: " + str(reverse(numbers)))
