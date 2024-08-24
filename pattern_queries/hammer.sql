WITH ranked_data AS (
    SELECT
        date,
        open,
        high,
        low,
        close,
        AVG(ABS(open - close)) OVER (ORDER BY date ROWS BETWEEN 10 PRECEDING AND 1 PRECEDING) AS avg_size
    FROM
        ohlc_data
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
    -- The candle is a short candle
    ABS(open - close) < avg_size * 0.8 AND

    -- But not a doji
    ABS(open - close) > avg_size * 0.1 AND

    -- With very short upper shadow
    high - GREATEST(open, close) < avg_size * 0.1 AND

    -- And lower shadow at least 2 times the size of the body
    LEAST(open, close) - low > ABS(open - close) * 2