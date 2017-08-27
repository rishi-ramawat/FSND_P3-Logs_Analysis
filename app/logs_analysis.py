#!/usr/bin/env python3


from database import Cursor
from database import Database


questionsAndQueriesList = [
    {
        "question": "What are the most popular three articles of all time?",
        "query": """
SELECT articles.title, COUNT(*) as views FROM log, articles
WHERE log.path = CONCAT('/article/', articles.slug)
AND log.status LIKE '%200%'
GROUP BY articles.title
ORDER BY views DESC
LIMIT 3;"""
    },
    {
        "question": "Who are the most popular article authors of all time?",
        "query": """
SELECT authors.name, COUNT(*) as views FROM log, authors, articles
WHERE log.path = CONCAT('/article/', articles.slug)
AND log.status LIKE '%200%'
AND articles.author = authors.id
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
        ) as errors FROM log
    GROUP BY day
    ORDER BY errors DESC
) as subQuery
WHERE errors > 1.0;"""
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
            field_names = [str(i[0]).upper() for i in cursor.description]

        print('### ' + listItem['question'], end='\n\n')
        print('| ' + ' | '.join(field_names) + ' |')
        print('| ' + ('--- | ' * len(field_names)))

        for result in results:
            print('| ' + ' | '.join(str(x) for x in result) + ' |')

        print('\r\n', end='')


if __name__ == '__main__':
    generateReport()
    Database.closeAllConnections()
