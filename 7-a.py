def hex_string_to_int(hex):
    val = 0
    for c in hex:
        val *= 16
        if c == 'a':
            val += 10
        elif c == 'b':
            val += 11
        elif c == 'c':
            val += 12
        elif c == 'd':
            val += 13
        elif c == 'e':
            val += 14
        elif c == 'f':
            val +=15
        else:
            val /= 16
            val = int(val)

    return val

while True:
    try:
        word = input()

        print(hex_string_to_int(word), word)
    except EOFError:
        break
