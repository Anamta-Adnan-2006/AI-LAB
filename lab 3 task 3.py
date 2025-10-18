def even_numbers(n):
    evens = []
    for i in range(1, n + 1):
        evens.append(i * 2)
    print("First", n, "even numbers are:", evens)
    return evens
n = int(input("Enter how many even numbers you want: "))
even_list = even_numbers(n)
sum_even = sum(even_list)
product_even = 1
for num in even_list:
    product_even *= num
3print("Sum of even numbers:", sum_even)
print("Product of even numbers:", product_even)
