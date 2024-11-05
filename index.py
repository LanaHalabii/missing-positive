def first_missing_positive(numbers):

    for i in range(1, len(numbers)+1):  
        if i not in numbers:            
            return i


numbers = [3, 4, -1, 1]
print(first_missing_positive(numbers))