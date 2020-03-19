# Write a function power() that given value a and exponent b will compute a^b
# It would be silly to have the function say return a^b, we won't learn anything

def power(value, exponent):
  # What is 2 ^ 3?
  # 2 * 2 * 2

  # problem 1
  # if exponent == 1:
  #   return value
  # Problem 2
  # if exponent == 2:
  #   return Problem1value * value
  # Problem 3
  # if exponent == 3:
  #   return Problem2Value * value
  # Problem 4
  # if exponent == 4:
  #   return Prob3Value * value

  # What about negative?
  # X ^ -n == 1 / x ^ n

  if exponent < 0:
    exponent *= -1
    value = 1 / value

  # What about fractions??
  if not exponent.is_integer():
    print('Sorry, this feature is premium.')
    return
    
  if exponent == 0:
    return 1

  return value * power(value, exponent - 1)

print(power(4, 1/2))