WITH ranked_data AS (
    SELECT
        date,
        open,
        high,
        low,
        close,
        LAG(close, 1) OVER (ORDER BY date) AS prev_close,
        LAG(close, 2) OVER (ORDER BY date) AS prev2_close,
        LAG(open, 1) OVER (ORDER BY date) AS prev_open,
        LAG(open, 2) OVER (ORDER BY date) AS prev2_open,
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
    -- First candle is long white
    (prev2_close - prev2_open) > avg_size AND

    -- Second candle is a short candle
    ABS(prev_open - prev_close) < avg_size * 0.8 AND

    -- But not a doji
    ABS(prev_open - prev_close) > avg_size * 0.1 AND

    -- That gaps up above the first and third candle
    LEAST(prev_open, prev_close) > prev2_close AND
    LEAST(prev_open, prev_close) > open AND

    -- Third candle is long black
    (open - close) > avg_size;
