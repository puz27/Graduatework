from request_manager import RequestManager
from data_base_manager import DBManager
from utils import config
from utils import prepare_problem_format
import requests

# prepare bases and add info to it
connection_params = config()
data_base = DBManager(connection_params, "codeforces_base")
codeforces_data = RequestManager()
# data_base.create_database("codeforces_base")
# data_base.create_tables()

# get_problems_data = codeforces_data.problems_data
# data_base.insert_data("problems", get_problems_data)



# work with requests
# xxx = [['1u', 'Theatre Square', None, 1000, 219574, ['math'], 'PROGRAMMING'], ['1jy', 'Theatre Square', None, 1000, 219574, ['math'], 'PROGRAMMING']]
codeforces_data.get_request()
for problem in codeforces_data.problems_data:
    data_base.check_id("problems", problem)


# get_problems_data = codeforces_data.problems_data
# xxx = [['1A', 'Theatre Square', None, 1000, 219574, ['math'], 'PROGRAMMING']]
# data_base.insert_data("problems", xxx)
# data_base.insert_data("problems", get_problems_data)












# x = [[1857, 'F', 'Sum and Product', None, 1600, 7879, ['binary search', 'data structures', 'math'], 'PROGRAMMING'], [1111, 'F', 'Sum and Product', None, 1600, 7879, ['binary search', 'data structures', 'math'], 'PROGRAMMING']]
# ddd = [[1857, 'F', 'Sum and Product', 'PROGRAMMING', 1600, 7879, ['binary search', 'data structures'], 'math']]

download_dict = {'contestId': 1, 'index': 'B', 'name': 'Spreadsheet', 'type': 'PROGRAMMING', 'rating': 1600, 'tags': ['implementation', 'math']}

# prepares_dict = {
#     'contestId': str(download_dict["contestId"]) + str(download_dict["index"]),
#     'name': download_dict["name"],
#     'points': download_dict["points"],
#     'rating': download_dict["rating"],
#     'solvedCount': download_dict["solvedCount"],
#     'tags': download_dict["tags"],
#     'type': download_dict["type"]
# }


# def prepare_problem_format2(problem: dict) -> list:
#     default_tags = ('contestId', 'index', 'name', 'type', 'rating', 'solvedCount', 'tags', 'points')
#     default_tags = ('name', 'type', 'rating', 'solvedCount', 'tags', 'points')
#     for tag in default_tags:
#         problem.setdefault(tag)
#
#     prepared_dict = {
#         'contestId': str(problem["contestId"]) + str(problem["index"]),
#         'name': problem["name"],
#         'points': problem["points"],
#         'rating': problem["rating"],
#         'solvedCount': problem["solvedCount"],
#         'tags': problem["tags"],
#         'type': problem["type"]
#     }
#     return list(prepared_dict.values())


# print(prepare_problem_format2(slovar))
#
# url_problemset = "https://codeforces.com/api/problemset.problems"
# response = requests.get(url_problemset)
# if response.status_code == 200:
#     if response.status_code == 200:
#
#         for problem in response.json()["result"]["problems"]:
#             print(problem)
#             contestId = problem["contestId"]
#             index = problem["index"]
#             print(contestId, index)
#
# # select * from problems
# # where contestid = 1872 and index = 'G'

