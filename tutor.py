# This is a prompt which will be used to enter the first number
# we will convert it from string to integer after the user enter the number
target = int(input('please enter the first number:'))

# we will initialize an empty list for all the numbers to store
numbers =[]

# we will also create a variable which store the value 0
end_list = 0

# this is a print statement
print('Please enter the number or leave it blank when there is no additional number:')

# we will continously prompt user to enter the value until the user leave it blank
# this will end the continuous loop by making end_list = 1
# as long as the user enter a value, it will continue the loop since end_list = 0
while end_list == 0:
    integer = input('numbers:')
    if integer == '':
        end_list = 1
    else:
        numbers.append(int(integer)) # we will add the value to the initialized list


# we will first remove duplicate values and then sort it by ascending order
# note that sort is not important here but it is used to allow user to look through
# the value more clearly
sorted(set(numbers))
print('This is the list of numbers:')
print(numbers)


# we then create a new function with the first number which we named as target
# and the list of numbers as numbers
# we create an empty list which will be used to store pair that has sum of the 
# first number 
def target_pair(numbers,target):
    pair_list = []

    # since we are finding pairs with sum of the first number which is the target
    # we first start iterate through the list for the first value, 'i' of the pair
    for i in numbers:

        # we then iterate through the list for the second value, 'k' of the pair
        for k in numbers:

            # we set 2 condition where first and second value of the pair must
            # equal to the first number which is the target
            # we also  don't want to have value of their own as a pair which is
            # labeled as i != k
            if i + k == target and i != k:
                
                # we create an temporary empty list for the current loop 
                # and append the pair to the temporary list then sort it
                listed = []
                listed.extend((i,k))
                listed.sort()
                
                # we want to make sure that there is no duplicates in the list 
                # when we append the list into the final list.
                if listed not in pair_list:
                    pair_list.append(listed)
    
    # we print each pair as a new lines
    for pair in pair_list:
        print(pair)

# this is used to run the function above.
target_pair(numbers,target)
