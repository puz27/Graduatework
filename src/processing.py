from src.dictionary import user_questions
from src.request_manager import RequestManager
from src.data_base_manager import DBManager
from src.utils import config
from bot.bot import main_bot
import asyncio


def main_processing() -> None:
    while True:
        print(*user_questions)
        user_answer = input()
        if user_answer == user_questions["3.End program."]:
            break
        if user_answer == user_questions["2.Second running. (Bases already exist.)\n"]:
            asyncio.run(main_bot())
        if user_answer == user_questions[" 1.First running.(Create and prepare bases.)\n"]:
            # prepare bases and add info to it
            print("Prepare bases. Waiting near 5 minutes...")
            connection_params = config(section="postgresql")
            data_base = DBManager(connection_params, "codeforces_base")
            codeforces_data = RequestManager()

            data_base.create_database("codeforces_base")
            data_base.create_tables()

            codeforces_data.get_request()
            get_problems_data = codeforces_data.problems_data
            data_base.insert_data("problems", get_problems_data)
            asyncio.run(main_bot())


