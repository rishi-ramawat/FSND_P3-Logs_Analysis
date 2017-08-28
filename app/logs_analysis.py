#!/usr/bin/env python3


from database import Cursor
from database import Database


questionsAndQueriesList = [
    {
        "question": "What are the most popular three articles of all time?",
        "query": """
SELECT articles.title, popular_pages.views FROM articles
INNER JOIN popular_pages
ON popular_pages.path = CONCAT('/article/', articles.slug)
ORDER BY popular_pages.views DESC
LIMIT 3;"""
    },
    {
        "question": "Who are the most popular article authors of all time?",
        "query": """
SELECT authors.name, SUM(popular_pages.views) as views FROM authors
INNER JOIN articles
ON articles.author = authors.id
INNER JOIN popular_pages
ON popular_pages.path = CONCAT('/article/', articles.slug)
GROUP BY authors.name
ORDER BY views DESC;"""
    },
    {
        "question":
            'On which days did more than 1% of requests lead to errors?',
        "query": """
SELECT * FROM (
    SELECT DATE(time) as day,
        ROUND (
            (
                100.0 * SUM (
                    CASE log.status WHEN '200 OK' THEN 0 ELSE 1 END
                )
            ) / COUNT(log.status),
            3
        ) as errors_in_percentage FROM log
    GROUP BY day
    ORDER BY errors_in_percentage DESC
) as subQuery
WHERE errors_in_percentage > 1.0;"""
    }
]


def generateReport():
    """
        Generates a report of answers to the questions
        in the questionsAndQueriesList
    """
    for listItem in questionsAndQueriesList:
        with Cursor() as cursor:
            cursor.execute(listItem['query'].replace('\n', ' '))
            results = cursor.fetchall()
            field_names = [
                str(i[0]).replace('_', ' ').upper() for i in cursor.description
            ]

        print('### ' + listItem['question'], end='\n\n')
        print('| ' + ' | '.join(field_names) + ' |')
        print('| ' + ('--- | ' * len(field_names)))

        for result in results:
            print('| ' + ' | '.join(str(x) for x in result) + ' |')

        print('\r\n', end='')


if __name__ == '__main__':
    generateReport()
    Database.closeAllConnections()
