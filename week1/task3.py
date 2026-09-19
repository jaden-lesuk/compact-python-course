if __name__ == '__main__':
    zahl = 10
    kommazahl = 10.5
    text = "Hello World"
    wahrheitwert = True

    print(type(zahl))
    print(type(kommazahl))
    print(type(text))
    print(type(wahrheitwert))

    float_zahl = float(zahl)
    print(float_zahl, type(float_zahl))

    int_kommazahl = int(kommazahl)
    print(int_kommazahl, type(int_kommazahl))

    string_zahl = str(zahl)
    print(string_zahl, type(string_zahl))

    string_to_num = int("12")
    print(string_to_num, type(string_to_num))

    int_to_bool = bool(12)
    print(int_to_bool, type(int_to_bool))