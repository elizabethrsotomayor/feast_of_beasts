def feast(beast, dish):
    first_beast = beast[0]
    last_beast = beast[-1]

    first_dish = dish[0]
    last_dish = dish[-1]

    if first_beast == first_dish and last_beast == last_dish:
        return True
    else:
        return False
