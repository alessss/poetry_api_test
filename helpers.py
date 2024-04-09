def get_real_lines_count(list_lines):
    return sum(1 for line in list_lines if len(line) > 0)