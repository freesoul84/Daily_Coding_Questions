--https://datalemur.com/questions/sql-histogram-tweets

SELECT 
  COUNT(*) AS tweet_bucket, A.count as users_num 
FROM (SELECT 
        COUNT(tweet_id) FROM tweets 
      WHERE EXTRACT(YEAR FROM tweet_date) = 2022 
      GROUP BY user_id) A
GROUP BY A.count
ORDER BY tweet_bucket