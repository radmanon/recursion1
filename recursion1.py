def is_power_of(number, base):
  # Base case: when number is smaller than base.
  number = number/base
  if number < base:
    # If number is equal to 1, it's a power (base**0).
    return False
  else:
    return True

  # Recursive case: keep dividing number by base.
  return is_power_of(number, base)

print(is_power_of(4,2)) # Should be True
print(is_power_of(9,3)) # Should be True
print(is_power_of(70,20)) # Should be False