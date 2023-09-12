from src.request_manager import RequestManager
from src.data_base_manager import DBManager
from src.utils import config
from bot.bot import main_bot
import asyncio
import schedule
import time
from apscheduler.schedulers.blocking import BlockingScheduler

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
# data_base.insert_new_data("problems", get_problems_data)


def some_jo():
    print("22222222222222222222222222222222222222222")


async def some_job():
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    # await schedule.every().minute.do(some_jo)

    # scheduler = BlockingScheduler()
    # scheduler.add_job(some_jo, 'interval', hours=1)
    # scheduler.start()

# find data in base
# search_problem = data_base.get_problems("problems", 800, "implementation", 10)
# for problem in search_problem:
#     print(problem)


async def foo():
    print("Start foo")
    await asyncio.sleep(1)
    print("End foo")


async def bar():
    print("Start bar")
    await asyncio.sleep(2)
    print("End bar")


async def main():
    await asyncio.gather(foo(), bar(), main_bot())


asyncio.run(main())


# asyncio.run(some_job())
# asyncio.run(main_bot())
