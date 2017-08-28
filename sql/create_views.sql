-- The following SQL queries create database views required to run the app.
--
-- Author: RISHI RAMAWAT
-- Date: 2017-08-28

CREATE OR REPLACE VIEW popular_pages AS (
    SELECT path, count(*) AS views
    FROM log
    WHERE status = '200 OK'
    GROUP BY path
);
