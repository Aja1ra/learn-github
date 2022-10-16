def remove_asterisk(string):
    new_string = ''
    if '*' in string:
        for i, k in enumerate(string):
            if k == '*':
                new_string += "#"
            else:
                new_string += k

    return new_string

print(remove_asterisk('sk*f*s*df'))
