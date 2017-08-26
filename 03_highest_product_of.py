def my_function(list_of_ints):
    highest = max(list_of_ints[0:3])
    lowest = min(list_of_ints[0:3])
    lowest_product_two = list_of_ints[0] * list_of_ints[1]
    highest_product_two = lowest_product_two
    highest_product_of_3 = lowest_product_two * list_of_ints[2]
    
    for x in list_of_ints[2:]:
        highest_product_of_3 = max(x*highest_product_two, x*lowest_product_two, highest_product_of_3)
        highest_product_two = max(highest_product_two, x*highest, x*lowest)
        lowest_product_two = min(lowest_product_two, x*highest, x*lowest)
        highest = max(x, highest)
        lowest = min(x, lowest)

    return highest_product_of_3

print(my_function([-10, -10, 1, 3, 2]))
