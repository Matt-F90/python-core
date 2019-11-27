def count_upper_case(message):
    return sum([1 for c in message if c.isupper()])
print(count_upper_case("Hello, World!"))

assert count_upper_case("") == 0, "Empty String"
assert count_upper_case("A") == 1, "One Uppercase"
assert count_upper_case("a") == 0, "One Lowercase"
assert count_upper_case("£$%^&") == 0, "Special Characters"
assert count_upper_case("GOOD bad") == 4, "Uppercase and Lowercase mix"
assert count_upper_case("12345") == 0, "Numbers"
print("all tests passed")