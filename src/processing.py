from src.request_manager import RequestManager
from src.data_base_manager import DBManager
from src.utils import config
from bot.bot import main_bot
import asyncio
import schedule
import time
from apscheduler.schedulers.blocking import BlockingScheduler
import datetime

# prepare bases and add info to it
connection_params = config()
data_base = DBManager(connection_params, "codeforces_base")
codeforces_data = RequestManager()

# data_base.create_database("codeforces_base")
# data_base.create_tables()
#
# codeforces_data.get_request()
# get_problems_data = codeforces_data.problems_data
# data_base.insert_data("problems", get_problems_data)


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
# asyncio.run(main())
