from configparser import ConfigParser
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


def prepare_problem_format(problem: dict) -> list:
    """
    Prepare data before load to base. ContestId will consist from contestId and index. Tags convert to str.
    :param problem: dictionary with one problem
    :return: list with problem.
    """
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
        }
    return list(prepared_dict.values())


def open_query_file(file_path: str) -> str:
    """
    Open file with creation table query
    :param file_path: path to file
    :return: query
    """
    try:
        query_file = os.path.join(os.getcwd(), f"{os.path.dirname(os.path.dirname(os.path.abspath(__file__)))}{file_path}")
        with open(query_file, "r", encoding='utf-8') as read_file:
            query_create_tables = read_file.read()
            return query_create_tables
    except FileNotFoundError as error:
        print(f"Can not find file with queries:{error}")


def execute_bot_insert_name(search_name: str):
    return search_name.replace("'", "")
