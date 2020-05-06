def is_blank(lines, x, y):
    if lines == 1:
        return False
    elif x in range(lines // 3, lines // 3 * 2) and y in range(
            lines // 3, lines // 3 * 2):
        return True
    else:
        return is_blank(lines // 3, x % (lines // 3), y % (lines // 3))


def carpet(lines, input):
    output = ''
    for x in range(lines):
        for y in range(lines):
            if not is_blank(lines, x, y):
                output += input
            else:
                output += '  '
            if x != lines - 1 and y == lines - 1:
                output += '\n'
    return output


print(carpet(9, '草'))
