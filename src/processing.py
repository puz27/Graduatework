from src.dictionary import user_questions
from src.request_manager import RequestManager
from src.data_base_manager import DBManager
from src.utils import config
from bot.bot import main_bot
import asyncio

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





# codeforces_data.get_request()
# get_problems_data = codeforces_data.problems_data
# for problem in get_problems_data:
#     data_base.insert_new_data("problems", problem)


# find data in base
# search_problem = data_base.get_problems("problems", 800, "implementation", 10)
# for problem in search_problem:
#     print(problem)


# async def display_date():
#     loop = asyncio.get_running_loop()
#     end_time = loop.time() + 999
#
#     while True:
#         if loop.time() >= end_time:
#             break
#         await asyncio.sleep(600)
#         print("Make request for update base.")
#         codeforces_data.get_request()
#         get_problems_data = codeforces_data.problems_data
#         for problem in get_problems_data:
#             data_base.insert_new_data("problems", problem)

#
#
# async def main():
#     await asyncio.gather(display_date(), main_bot())
#
#


