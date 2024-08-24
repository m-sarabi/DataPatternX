patterns = {
    'HAMMER': 'pattern_queries/sql_files/hammer.sql',

    'ENGULFING_BULLISH': 'pattern_queries/sql_files/engulfing_bullish.sql',
    'ENGULFING_BEARISH': 'pattern_queries/sql_files/engulfing_bearish.sql',

    'MORNING_STAR': 'pattern_queries/sql_files/morning_star.sql',
    'EVENING_STAR': 'pattern_queries/sql_files/evening_star.sql',

    'THREE_WHITE_SOLDIERS': 'pattern_queries/sql_files/three_white_soldiers.sql',
    'THREE_BLACK_CROWS': 'pattern_queries/sql_files/three_black_crows.sql',
}


def get_pattern(pattern_name):
    return patterns.get(pattern_name)


def list_patterns():
    return list(patterns.keys())