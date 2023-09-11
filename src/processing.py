from request_manager import RequestManager
from data_base_manager import DBManager
from utils import config
from utils import prepare_problem_format
import requests


# prepare bases and add info to it
connection_params = config()
data_base = DBManager(connection_params, "codeforces_base")
codeforces_data = RequestManager()

data_base.create_database("codeforces_base")
data_base.create_tables()
#
codeforces_data.get_request()
get_problems_data = codeforces_data.problems_data
data_base.insert_data("problems", get_problems_data)


# check every hour
# codeforces_data.get_request()
# get_problems_data = codeforces_data.problems_data
# data_base.insert_new_data("problems", get_problems_data)

# find data in base
# search_problem = data_base.get_problems("problems", 800, "implementation", 10)
# for problem in search_problem:
#     print(problem)

