some_list = [2 ,7 ,9 ,8 ,88 ,90 , 91,]
one_list = []

def even_number_of_evens(my_list, even_numbers):
    for number in my_list:
        if number % 2 == 0:
            even_numbers.append(number)
    
    
    length = len(even_numbers)
    if not length % 2 == 0:
        print("this is not an even number of evens")
    else:
        print(even_numbers)
        return even_numbers
        

even_number_of_evens(some_list, one_list)
       

# assert even_number_of_evens([]) == False, "No numbers"   
# assert even_number_of_evens([2]) == False, "One even number"
# assert even_number_of_evens([2, 4]) == True, "Two even numbers"
# assert even_number_of_evens([2, 3]) == False, "Two numbers, only one even"
# assert even_number_of_evens([2, 3, 9, 10, 13, 7, 8]) == False, "Multiple numbers, three even"
# assert even_number_of_evens([2, 3, 9, 10, 13, 7, 8, 5, 12]) == True, "Multiple numbers, four even"
# assert even_number_of_evens([1, 3, 9]) == False, "No even numbers"

print("All tests passed!")