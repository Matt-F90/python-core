def test_function(numbers):
    return 3

def test_are_equal(actual, expected):
    assert actual == expected, "Expected {0}, got {1}".format(expected, actual)

def test_are_not_equal(a, b):
    assert a != b, "Did not expect {0}, but got {1}".format(a, b)
    
def test_is_in_collection(collection, item):
    assert item in collection, "{0} does not contain {1}".format(collection, item)
    
test_is_in_collection(test_function([1, 2, 3, 4, 5]), 3)