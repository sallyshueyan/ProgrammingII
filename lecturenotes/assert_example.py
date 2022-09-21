def is_odd(number):
    return number % 2 == 1  # will always return False (always)


if __name__ == '__main__':
    print("-- Start of the tests --")
    assert is_odd(33), "33 should return True, not False"
    assert not is_odd(100), "100 should return False, not True"
    print("--End of Tests--")
