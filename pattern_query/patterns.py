import os

SQL_DIR = "pattern_query/sql_files"
patterns = {
    os.path.splitext(file)[0].upper(): os.path.join(SQL_DIR, file)
    for file in os.listdir(SQL_DIR)
    if file.endswith('.sql')
}


def get_pattern(pattern_name):
    return patterns.get(pattern_name)


def list_patterns():
    return list(patterns.keys())
