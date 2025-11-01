nums = input('Enter elements of a list separated by space \n')
target = int(input("Enter a number that can only be the sum of two numbers from the previously entered list \n"))

user_list = nums.split()
# convert each item to int type
for i in range(len(user_list)):
    user_list[i] = int(user_list[i])

j = 1
output = []
for i in user_list:
    difference = target - i
    if difference >= 0:
        while j < len(user_list):
            if difference - user_list[j] == 0:
                output.append(user_list.index(i))
                output.append(j)
            j += 1
        j = user_list.index(i) + 1
if len(output) == 2:
    print("Output: " + str(output))
elif len(output) > 2:
    print("There are more than 2 numbers that add up to " + str(target))
else:
    print("There are not 2 numbers that add up to " + str(target))

