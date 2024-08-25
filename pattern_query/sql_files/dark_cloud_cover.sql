WITH ranked_data AS (
    SELECT
        date,
        open,
        high,
        low,
        close,
        LAG(close, 1) OVER (ORDER BY date) AS prev_close,
        LAG(open, 1) OVER (ORDER BY date) AS prev_open,
        LAG(high, 1) OVER (ORDER BY date) AS prev_high,
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
    -- First candle is long white
    (prev_close - prev_open) > avg_size AND

    -- Second candle is black
    open > close AND

    -- That opens above the previous high
    open > prev_high AND

    -- And closes below the midpoint of the previous candle
    close < (prev_open + prev_close) / 2
