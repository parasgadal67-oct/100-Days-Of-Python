#data filtering through list comprehension.

# filtering the even and odd numbers.
numbers = [1, 2, 3, 4, 5, 6, 7, 98, 90, 48]
even_nums = [num for num in numbers if num %2 ==0 ]
print(even_nums)

odd_nums = [num for num in numbers if num % 2 ==1]
print(odd_nums)
