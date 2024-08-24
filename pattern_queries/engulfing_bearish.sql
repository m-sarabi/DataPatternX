WITH ranked_data AS (
    SELECT
        date,
        open,
        high,
        low,
        close,
        LAG(open, 1) OVER (ORDER BY date) AS prev_open,
        LAG(close, 1) OVER (ORDER BY date) AS prev_close,
        AVG(ABS(open - close)) OVER (ORDER BY date ROWS BETWEEN 10 PRECEDING AND 1 PRECEDING) AS avg_size
    FROM
        {{TABLE_NAME}}
)
SELECT
    date,
    open,
    high,
    low,
    close,
    avg_size
FROM
    ranked_data
WHERE
    -- First candle is white
    prev_open < prev_close AND

    -- Second candle is black
    open > close AND

    -- That engulfs the first candle
    open > prev_close AND
    close < prev_open;