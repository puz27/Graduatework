from configparser import ConfigParser
import psycopg2
import os


def config(section, filename=f"{os.path.dirname(os.path.dirname(os.path.abspath(__file__)))}/database.ini") -> dict:
    """
    Get configuration for connection to database
    :param filename: name of configuration file
    :param section: name of section in configuration file
    :return:
    """
    parser = ConfigParser()
    parser.read(filename)
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception(f'Section {section} did not find in configuration file.')
    return db


def connection_to_db(connection_params: dict, query_db: str) -> None:
    """
    Connect to database
    :param connection_params: configuration for connection
    :param query_db: query to database
    :return:
    """
    try:
        connection = psycopg2.connect(**connection_params)
        try:
            with connection:
                with connection.cursor() as cursor:
                    query = query_db
                    cursor.execute(query)
                    connection.commit()
        except psycopg2.Error as er:
            print(f"Error query.\n{er}")
        finally:
            connection.close()
    except psycopg2.OperationalError as er:
        print(er)


def prepare_problem_format(problem: dict) -> list:
    """
    Prepare data before load to base. ContestId will consist from contestId and index. Tags convert to str.
    :param problem: dictionary with one problem
    :return: list with problem.
    """
    print (problem)
    default_tags = ('name', 'type', 'rating', 'solvedCount', 'tags', 'points')
    for tag in default_tags:
        problem.setdefault(tag)

    prepared_dict = {
        'contestId': str(problem["contestId"]) + str(problem["index"]),
        'name': problem["name"],
        'points': problem["points"],
        'rating': problem["rating"],
        'solvedCount': problem["solvedCount"],
        'tags': " ".join(problem["tags"]),
        'type': problem["type"]
    }
    print(list(prepared_dict.values()))
    return list(prepared_dict.values())

