import psycopg2
import os
from src.utils import connection_to_db


class DBManager:
    """ Class connects and works with bases"""
    def __init__(self, connection_params: dict, database=None):
        self.__database = database
        self.__connection_params = connection_params

    def create_database(self, new_database: str) -> None:
        """
        Create new database
        :param new_database:  name of new database
        :return:
        """
        try:
            connection = psycopg2.connect(**self.__connection_params)
            connection.autocommit = True

            # Create database
            try:
                with connection.cursor() as cursor:
                    query_create_base = f"CREATE DATABASE {new_database}"
                    cursor.execute(query_create_base)
                    self.__database = new_database
                    print(f"База данных {new_database} успешно создана.")
            except Exception as er:
                print(f"БД:{new_database}. Ошибка с запросом создания БД.\n{er}")
            finally:
                connection.close()
        except psycopg2.OperationalError as er:
            print(er)

    def create_tables(self) -> None:
        """
        Create new tables
        :return:
        """
        try:
            self.__connection_params.update({'dbname': self.__database})
            connection = psycopg2.connect(**self.__connection_params)

            # Read file with queries
            try:
                query_file = os.path.join(os.getcwd(), "../sql/queries.sql")
                print(query_file)
                with open(query_file, "r", encoding='utf-8') as read_file:
                    query_create_tables = read_file.read()
            except FileNotFoundError as error:
                print(f"Файл с запросами не найден:{error}")

            # Create tables
            try:
                with connection:
                    with connection.cursor() as cursor:
                        cursor.execute(query_create_tables)
                        connection.commit()
                        print(f"Создание таблиц прошло успешно.")
            except Exception as er:
                print(f"Ошибка с запросом при создании таблиц.\n{er}")
            finally:
                connection.close()
        except psycopg2.OperationalError as er:
            print(er)

    def insert_data(self, table: str, data: list) -> None:
        """
        Insert new data to database
        :param table: table name for insert
        :param data: list with data for processing
        :return:
        """
        try:
            self.__connection_params.update({'dbname': self.__database})
            connection = psycopg2.connect(**self.__connection_params)

            try:
                with connection:
                    with connection.cursor() as cursor:
                        col_count = "".join("%s," * len(data[0]))
                        print(col_count)

                        query = f"INSERT INTO {table} VALUES ({col_count[:-1]})"
                        cursor.executemany(query, data)
                        connection.commit()
                        print(f"Операция над таблицей {table} прошла успешно.")
            except psycopg2.Error as er:
                print(f"Ошибка с запросом.\n{er}")
            finally:
                connection.close()
        except psycopg2.OperationalError as er:
            print(er)

    def insert_new_data(self, table: str, problem: list) -> None:

        try:
            self.__connection_params.update({'dbname': self.__database})
            connection = psycopg2.connect(**self.__connection_params)

            try:
                with connection:
                    with connection.cursor() as cursor:
                        col_count = "".join("%s," * len(problem))
                        query_search = f"""
                                select contestId from problems
                                where contestId = '{problem[0]}'
                                """
                        query_insert = f"INSERT INTO {table} VALUES ({col_count[:-1]})"

                        cursor.execute(query_search)
                        connection.commit()
                        get_id = cursor.fetchone()
                        if get_id is None:
                            print(problem, "No in base. Must add!")
                            cursor.execute(query_insert, problem)
                            connection.commit()

            except psycopg2.Error as er:
                print(f"Ошибка с запросом.\n{er}")
            finally:
                connection.close()
        except psycopg2.OperationalError as er:
            print(er)

    def get_problems(self,  table: str, rating: int, tag: str, limit: int) -> None:

        try:
            self.__connection_params.update({'dbname': self.__database})
            connection = psycopg2.connect(**self.__connection_params)

            try:
                with connection:
                    with connection.cursor() as cursor:
                        query_search = f"""
                                select * from problems
                                where rating = {rating} and tags = '{tag}'
                                LIMIT {limit}
                                """
                        cursor.execute(query_search)
                        connection.commit()
                        get_problems = cursor.fetchall()

            except psycopg2.Error as er:
                print(f"Ошибка с запросом.\n{er}")
            finally:
                connection.close()
                return get_problems
        except psycopg2.OperationalError as er:
            print(er)

    def get_problem_by_name(self,  table: str, problem_name: str, limit: int) -> None:

        try:
            self.__connection_params.update({'dbname': self.__database})
            connection = psycopg2.connect(**self.__connection_params)

            try:
                with connection:
                    with connection.cursor() as cursor:
                        query_search = f"""
                        select * from {table}
                        where name = '{problem_name}'
                        """
                        cursor.execute(query_search)
                        connection.commit()
                        get_problems = cursor.fetchall()

            except psycopg2.Error as er:
                print(f"Ошибка с запросом.\n{er}")
            finally:
                connection.close()
                return get_problems
        except psycopg2.OperationalError as er:
            print(er)



