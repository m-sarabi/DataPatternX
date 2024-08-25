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
        LAG(high, 1) OVER (ORDER BY date) AS prev_high,
        LAG(high, 2) OVER (ORDER BY date) AS prev2_high,
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
    -- All candles are long black
    (prev2_open - prev2_close) > avg_size AND
    (prev_open - prev_close) > avg_size AND
    (open - close) > avg_size AND

    -- With short upper shadow
    (prev2_high - prev2_open) < avg_size * 0.5 AND
    (prev_high - prev_open) < avg_size * 0.5 AND
    (high - open) < avg_size * 0.5 AND

    -- Each candle opens/close below the previous open/close
    prev_open < prev2_open AND
    prev_close < prev2_close AND
    open < prev_open AND
    close < prev_close;