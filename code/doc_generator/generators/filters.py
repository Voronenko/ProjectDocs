LEVEL_MAPPING = {
    0: '=',
    1: '=',
    2: '-',
    3: '^',
    4: '~',
}


def indentation(value):
    rv = value.replace('\n', '\n\n    ')
    return rv


def headings(value, level=0):
    rv = ''
    underline = '{}'.format(LEVEL_MAPPING[level] * len(value))
    if level == 0:
        rv = '{}\n'.format(underline)
    rv += '{}\n{}'.format(value, underline)
    return rv


def null_boolean(value):
    if value:
        return 'Yes'
    elif value is None:
        return 'N/A'
    return 'No'
