# Reduces a fraction to lowest common terms
def fraction_reducer(numerator, denominator):
    shared_divisors = []
    if numerator <= denominator:
        for i in range(1, denominator + 1):
            if numerator % i == 0 and denominator % i == 0:
                shared_divisors.append(i)
    elif denominator < numerator:
        for i in range(1, numerator + 1):
            if numerator % i == 0 and denominator % i == 0:
                shared_divisors.append(i)
    reduced_numerator = numerator//shared_divisors[len(shared_divisors)-1]
    reduced_denominator = denominator//shared_divisors[len(shared_divisors)-1]
    if numerator != reduced_numerator:
        print('The fraction {}/{} can be reduced to {}/{}'.format(numerator, denominator, reduced_numerator, reduced_denominator))
    else:
        print('The fraction {}/{} cannot be reduced'.format(numerator, denominator))

# Converts a fraction to a mixed number
def make_mixed_number(numerator, denominator):
    if numerator < denominator:
        print('The fraction {}/{} cannot be converted to a mixed number'.format(numerator, denominator))
    else:
        whole_part = numerator//denominator
        fraction_part = numerator % denominator
        print('The fraction {}/{} can be written as {} {}/{}'.format(numerator, denominator, whole_part, fraction_part, denominator))

# Finds the greatest common divisor of two numbers, for use in adding fractions
def gcd(number1, number2):
    shared_divisors = []
    if number1 < number2:
        for i in range(1, number2 + 1):
            if number1 % i == 0 and number2 % i == 0:
                shared_divisors.append(i)
    elif number2 <= number1:
        for i in range(1, number1 + 1):
            if number1 % i == 0 and number2 % i == 0:
                shared_divisors.append(i)
    return shared_divisors[len(shared_divisors) - 1]

# Calculates the sum of two fractions
def fraction_addition(numerator1, denominator1, numerator2, denominator2):
    lcm = abs(denominator1 * denominator2)//(gcd(denominator1, denominator2))
    changed_numerator1 = numerator1 * (lcm//denominator1)
    changed_numerator2 = numerator2 * (lcm//denominator2)
    final_sum = changed_numerator1 + changed_numerator2
    print('The sum of {}/{} + {}/{} is {}/{}'.format(numerator1, denominator1, numerator2, denominator2, final_sum, lcm))

# fraction_reducer(1,7)
# make_mixed_number(215, 31)
fraction_addition(-6, 13, 7, 41)