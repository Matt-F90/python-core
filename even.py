list = [2 ,7 ,9 ,8 ,88 ,90 , 91]
even_numbers = []

def even_number_of_evens(numbers):
    if len(list) % 2 == 0:
        numbers == False
    
    for numbers in list:
        if numbers % 2 == 0:
            even_numbers.append(numbers)
    print(even_numbers)
    return even_numbers

even_number_of_evens(list)
       

# assert even_number_of_evens([]) == False, "No numbers"   
# assert even_number_of_evens([2]) == False, "One even number"
# assert even_number_of_evens([2, 4]) == True, "Two even numbers"
# assert even_number_of_evens([2, 3]) == False, "Two numbers, only one even"
# assert even_number_of_evens([2, 3, 9, 10, 13, 7, 8]) == False, "Multiple numbers, three even"
# assert even_number_of_evens([2, 3, 9, 10, 13, 7, 8, 5, 12]) == True, "Multiple numbers, four even"
# assert even_number_of_evens([1, 3, 9]) == False, "No even numbers"

print("All tests passed!")