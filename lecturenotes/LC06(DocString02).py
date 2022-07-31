def is_valid_label(label):
    """
    Determine if the input label matches the requirements:
    labels must start with a capital, have at least 5 characters and
    at least one number
    """
    if len(label) < 5:
        return False
    if not label[0].isupper():
        return False
    valid_label = False
    for char in label:
        if char.isnumeric():
            valid_label = True
    return valid_label


print(is_valid_label("High5"))  # True
