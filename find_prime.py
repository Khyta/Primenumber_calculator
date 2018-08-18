number = 2
while True:
    check_number = 2
    x = 1
    while x == 1:
        if number / check_number == round(number / check_number, 0) and check_number != number:
            print(number, "is not a prime number!", number,"/",check_number,"=",number/check_number)
            number += 1
            check_number = 2
        elif number / check_number != round(number / check_number, 0):
            check_number += 1
        else:
            print(number,"is a prime number")
            number += 1
            check_number = 2
