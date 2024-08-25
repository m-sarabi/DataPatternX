WITH ranked_data AS (
    SELECT
        date,
        open,
        high,
        low,
        close,
        LAG(close, 1) OVER (ORDER BY date) AS prev_close,
        LAG(open, 1) OVER (ORDER BY date) AS prev_open,
        LAG(low, 1) OVER (ORDER BY date) AS prev_low,
        AVG(ABS(open - close)) OVER (ORDER BY date ROWS BETWEEN 10 PRECEDING AND 1 PRECEDING) AS avg_size
    FROM
        {{TABLE_NAME}}
)
SELECT
    date,
    open,
    high,
    low,
    close
FROM
    ranked_data
WHERE
    -- First candle is black and not short
    (prev_open - prev_close) > avg_size * 0.8 AND

    -- Second candle is white and not short
    (close - open) > avg_size * 0.8 AND

    -- That opens below the previous low
    open < prev_low AND

    -- And closes above the midpoint of the previous candle
    close > (prev_open + prev_close) / 2;
