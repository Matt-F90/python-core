def count_upper_case(message):
    count = 0
    for c in message:
        if c.isupper():
            count += 1
    return count
    
print(count_upper_case("Hello, World!"))

assert count_upper_case("") == 0, "Empty String"
assert count_upper_case("A") == 1, "One Uppercase"
assert count_upper_case("a") == 0, "One Lowercase"
assert count_upper_case("$%^&") == 0, "Special Characters"
print("all tests passed")