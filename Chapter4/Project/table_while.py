number_a = 0
while number_a < 9:
    number_b = 0
    while number_b < (number_a + 1):
        number_b = number_b + 1
        print("%d * %d = %d" %(number_b, number_a + 1, number_b * (number_a+1)), end="\t")
    number_a = number_a + 1
    print()
