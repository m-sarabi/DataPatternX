# DataPatternX

## Overview

This starter kit is designed to help you quickly set up a project that connects to a database,
retrieves candlestick pattern data using complex queries, manages pattern files, and plots charts.
The project is modular and easy to extend, making it suitable for various applications.

## Features

- **Database Connection:** Easy database connection using `db/connection.py`.
- **Data Retrieval:** Retrieves data patterns from the database using complex SQL queries defined in `db/queries.py`.
- **Chart Plotting:** Plots charts using the data retrieved, implemented in `plotter/plot_chart.py`.
- **Main Integration:** Orchestrates all components in `DataPatternX.py`.

## Getting Started

### Prerequisites

- Python 3.x (tested with Python 3.12)
- PostgreSQL (or a serverless option such as Neon Serverless PostgreSQL)

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/starter-kit.git
    cd starter-kit
    ```

2. Install the required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

3. Set up your database. You can use a local SQL instance or a serverless option like Neon Serverless PostgreSQL.

### Configuration

To connect to a database like Neon Serverless PostgreSQL, add `.env` file with the following content:

```dotenv
DATABASE_URL=postgresql://[user]:[password]@[neon_hostname]/[dbname]?sslmode=require
```

## CLI Usage

To quickly get started with `DataPatternX.py` script, run the following command:

```bash
python DataPatternX.py --help
```

### List Available Patterns

To list all available candlestick patterns, run the following command:

```bash
python DataPatternX.py -l
```

To query candlestick patterns, run the following command. Results will be printed in the console.

```bash
python DataPatternX.py pattern_name -t table_name
```

> [!IMPORTANT]
> When using pattern names, the table name is required.

To plot the results, run the following command:

```bash
python DataPatternX.py pattern_name -t table_name -p
```

To save the results to a CSV file, run the following command:

```bash
python DataPatternX.py pattern_name -t table_name -s save_path
```

> [!TIP]
> All patterns are saved in the same file, with the name of the pattern appended to the results.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

*Thanks to the developers of Neon Serverless PostgreSQL for providing a flexible and scalable database solution.*
