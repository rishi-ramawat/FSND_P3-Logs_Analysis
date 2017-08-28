-- The following SQL queries provide the answers to the questions
-- that the reporting tool needs to provide in the Logs Analysis Project.
--
-- Author: RISHI RAMAWAT
-- Date: 2017-08-27

-- 1. What are the most popular three articles of all time?

-- Initial Solution:
-- SELECT articles.title, COUNT(*) as views FROM log, articles
-- WHERE log.path = CONCAT('/article/', articles.slug)
-- AND log.status LIKE '%200%'
-- GROUP BY articles.title
-- ORDER BY views DESC
-- LIMIT 3;

-- Refactored & Optimized Solution:
SELECT articles.title, popular_pages.views FROM articles
INNER JOIN popular_pages
ON popular_pages.path = CONCAT('/article/', articles.slug)
ORDER BY popular_pages.views DESC
LIMIT 3;

-- 2. Who are the most popular article authors of all time?

-- Initial Solution:
-- SELECT authors.name, COUNT(*) as views FROM log, authors, articles
-- WHERE log.path = CONCAT('/article/', articles.slug)
-- AND log.status LIKE '%200%'
-- AND articles.author = authors.id
-- GROUP BY authors.name
-- ORDER BY views DESC;

-- Refactored & Optimized Solution:
SELECT authors.name, SUM(popular_pages.views) as views FROM authors
INNER JOIN articles
ON articles.author = authors.id
INNER JOIN popular_pages
ON popular_pages.path = CONCAT('/article/', articles.slug)
GROUP BY authors.name
ORDER BY views DESC;

-- 3. On which days did more than 1% of requests lead to errors?

SELECT * FROM (
    SELECT DATE(time) as day,
        ROUND (
            (
                100.0 * SUM (
                    CASE log.status WHEN '200 OK' THEN 0 ELSE 1 END
                )
            ) / COUNT(log.status),
            3
        ) as errors FROM log
    GROUP BY day
    ORDER BY errors DESC
) as subQuery
WHERE errors > 1.0;
