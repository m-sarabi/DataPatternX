from argparse import RawDescriptionHelpFormatter

import argparse
from db.connection import DBConnection
from db.queries import QueryExecutor
from pattern_query.patterns import get_pattern, list_patterns
from plotter import plot_chart


def main(pattern_names, table, save_path: str = None, plot: bool = False):
    db_connection = DBConnection()
    try:
        query_executor = QueryExecutor(db_connection)
        # patterns = get_pattern(pattern_names)

        if plot:
            results, all_data = query_executor.execute_pattern_query(pattern_names, table, True)
            plot_chart.plot(all_data, patterns=results)
        else:
            results = query_executor.execute_pattern_query(pattern_names, table, False)

        if save_path:
            try:
                results.to_csv(save_path, index=False)
                print('Results saved to', save_path)
            except Exception as e:
                print('Error saving results:', e)
        elif not plot:
            for result in results:
                print(result.get('name'), 'Patterns:')
                print(result.get('df'))

    finally:
        db_connection.close_connection()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        formatter_class=RawDescriptionHelpFormatter,
        description='CandleQuery - Candlestick Pattern Query.'
    )
    # positional argument
    parser.add_argument('pattern_name', nargs='*',
                        help='Name or names of the candlestick patterns to query')
    parser.add_argument('-t', '--table', required=True, type=str,
                        help='Name of the table in database. required argument.')
    parser.add_argument('-l', '--list', action='store_true',
                        help='List all available candlestick patterns')
    parser.add_argument('-s', '--save', type=str,
                        help='Path to save the results in a CSV file')
    parser.add_argument('-p', '--plot', action='store_true',
                        help='Plot the results')

    args = parser.parse_args()

    if args.list:
        print('Available patterns:')
        for pattern in list_patterns():
            print(f'- {pattern}')

    elif args.pattern_name:
        print(args.pattern_name)
        main(args.pattern_name, args.table, save_path=args.save, plot=args.plot)

    else:
        parser.print_help()
