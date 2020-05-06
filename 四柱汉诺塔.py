def func(height, start, this, that, end):
    if height == 1:
        return 1
    elif height == 0:
        return 0
    else:
        return func(height - 2, start, this, end, that) + 3 + func(
            height - 2, that, this, start, end)


start = 'start'
this = 'this'
that = 'that'
end = 'end'
print(func(4, start, this, that, end))