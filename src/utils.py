from configparser import ConfigParser
import psycopg2


def config(filename="../database.ini", section="postgresql") -> dict:
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
        raise Exception(
            'Секция {0} не найдена в {1}.'.format(section, filename))
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
                    for company in (cursor.fetchall()):
                        print(*company)
        except psycopg2.Error as er:
            print(f"Ошибка с запросом.\n{er}")
        finally:
            connection.close()
    except psycopg2.OperationalError as er:
        print(er)