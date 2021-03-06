# Logs Analysis

A reporting tool that prints out reports (in plain text) based on the data in the database.

**Note:** This is a solution to project 3 of the [Udacity Full-Stack Web Developer Nanodegree Program][1]. In this project, we have to build a reporting tool that runs complex __SQL__ queries on a large database (__1.677 million+__ records!), and helps us draw business conclusions from data.

Installing Development Pre-Requisites
-------------------------------------

+ Install [Python 3.5+][3]
+ Install [python-dotenv][4]
+ Install [PostgreSQL 9.2+][8]
+ Install [psycopg2][9]

Installing The Project for Development / Testing on Linux
---------------------------------------------------------

+ Clone the repository:

    ```shell
    $ git clone git@github.com:rishi-ramawat/FSND_P3-Logs_Analysis.git
    $ cd FSND_P3-Logs_Analysis
    ```

+ Initialize the project:

    ```shell
    $ bin/init_project
    ```

    * This shell script will create an `.env` file for you.
    * It will also install/upgrade [python-dotenv][4] & [psycopg2][9].
    * **Note**: You might have to run this command with `sudo` as it tries to upgrade python packages.

+ Review `.env` and configure any required variables.
    * Make sure you have correct database credentials in the `.env` file before trying to run the project.

Installing The Project for Development / Testing on Windows
-----------------------------------------------------------

+ Clone the repo
+ Visit the folder where you have cloned the repo
    * Make a copy `.env.example` and name it as `.env`
    * Make sure all the required variables are present & initialized in `.env`
+ Make sure you have [python-dotenv][4] & [psycopg2][9] installed
    * You can run `pip3 install -U -r requirements.txt` to install/upgrade them automatically.

Setting Up The Database
-----------------------

+ In [PostgreSQL][8] create the `news` database.
    * `createdb news` command can be used to create the database if [PostgreSQL][8] is installed natively on your system.
+ Next, [download the newsdata.zip here][10].
    * You will need to unzip this file after downloading it.
    * The file inside is called `newsdata.sql`.
+ To load the data, use the command `psql -d news -f newsdata.sql`.
+ Next, run the following command to create **DATABASE VIEWS** required to run the app:
    * `psql -d news -f sql/create_views.sql`

Running the project
-------------------

Run the following command to generate the reports:

```shell
$ python3 app/logs_analysis.py
```

Project Scenario
----------------

You've been hired onto a team working on a newspaper site. The user-facing newspaper site frontend itself, and the database behind it, are already built and running. You've been asked to build an __internal reporting tool__ that will use information from the database to discover what kind of articles the site's readers like.

The database contains newspaper articles, as well as the web server log for the site. The log has a database row for each time a reader loaded a web page. Using that information, your code will answer questions about the site's user activity.

The program you write in this project will run from the command line. It won't take any input from the user. Instead, it will connect to that database, use SQL queries to analyze the log data, and print out the answers to some questions.

The database includes three tables:

+ The `authors` table includes information about the authors of articles.
+ The `articles` table includes the articles themselves.
+ The `log` table includes one entry for each time a user has accessed the site.

Project Highlights
------------------

+ This project implements a single query solution for each of the questions in hand.
    * When the application fetches data from multiple tables, it uses a single query with a join, rather than multiple queries.
    * See [app/logs_analysis.py][2] for more details.
+ The code conforms to the [PEP8][5] style recommendations.
+ The project outputs reports in [Markdown][6] format. See [OUTPUT.md][7] for more details.


[1]: https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd004 "Udacity Nanodegree: Full Stack Web Developer"
[2]: https://github.com/rishi-ramawat/FSND_P3-Logs_Analysis/blob/master/app/logs_analysis.py "Logs Analysis Python Code"
[3]: https://www.python.org/downloads/ "Download Python"
[4]: https://pypi.python.org/pypi/python-dotenv "python-dotenv"
[5]: https://www.python.org/dev/peps/pep-0008/ "PEP 8 -- Style Guide for Python Code | Python.org"
[6]: https://en.wikipedia.org/wiki/Markdown "Markdown - Wikipedia"
[7]: https://github.com/rishi-ramawat/FSND_P3-Logs_Analysis/blob/master/OUTPUT.md "OUTPUT.md"
[8]: https://www.postgresql.org/download/ "PostgreSQL: Downloads"
[9]: http://initd.org/psycopg/docs/install.html "Psycopg Documentation"
[10]: https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip "News Database Data"
