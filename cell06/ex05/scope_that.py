def add_one(value):
    return value + 1

if __name__ == "__main__":
    my_var = 5

    print("Before calling add_one:", my_var)
    my_var = add_one(my_var)

    print("After calling add_one:", my_var)