import itertools


def print_title(title, level=1):
    '''
    Title formatter for printing in terminal

    title: string to display
    level: level of the title (default 1)


    level 0 title

    ----- level 1 title -----

    |-------------------| LEVEL 2 TITLE |-------------------|

    |-----------------------------------------------|
    |-------------| LEVEL 3 TITLE |-----------------|
    |-----------------------------------------------|

    '''

    title_formats = {
        0: '\n{title}',
        1: '\n{5*"-"} {title} {5*"-"}',
        2: '\n|{20*"-"}| {upper(log)} |{20*"-"}|',
        3: '\n|{(44 + len(log))* "-"}|'
        '\n|{20*"-"}| {upper(log)} |{20*"-"}|'
        '\n|{(44 + len(log))* "-"}|',
    }

    print(title_formats[level].format(title))


def print_table(data):
    # extract rows and headers from data
    headers = set(itertools.chain.from_iterable(list(f.keys()) for f in data))
    rows = [[str(f[key]) for key in headers] for f in data]

    # compute lengths
    headers_lengths = [len(header) for header in headers]
    cell_lengths = [[len(cell) for cell in row] for row in rows]
    all_lengths = [headers_lengths] + cell_lengths
    max_col_width = [max(col) for col in zip(*all_lengths)]

    # prepare patterns
    col_patterns = ['{{:{}}}'.format(length) for length in max_col_width]
    separator = ' | '
    row_pattern = separator.join(col_patterns)
    table_width = sum(max_col_width) + (len(max_col_width) - 1) * len(separator)

    # prints
    print(row_pattern.format(*headers))
    print('-' * table_width)
    for row in rows:
        print(row_pattern.format(*row))
