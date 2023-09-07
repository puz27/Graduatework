from request_manager import RequestManager
from data_base_manager import DBManager
from utils import config
import requests

# work with base
connection_params = config()
data_base = DBManager(connection_params, "codeforces_base")
# data_base.create_database("codeforces_base")
# data_base.create_tables()


# work with requests
codeforces_data = RequestManager()
# codeforces_data.get_request()
# get_problems_data = codeforces_data.problems_data

# # zzz = [555, 'A', 'Winner', None, 1500, ['hashing', 'implementation'], 'PROGRAMMING'], [1, 'B', 'Spreadsheet', None, 1600, ['implementation', 'math'], 'PROGRAMMING']
# data_base.insert_data("problems", get_problems_data)

#
codeforces_data.get_request()
xxx = codeforces_data.problems_data
print(xxx)
data_base.insert_data("problems", xxx)

# url_problemset = "https://codeforces.com/api/problemset.problems"
# response = requests.get(url_problemset)
# print(response.json()["result"]["problems"])
# print(response.json())
# for i in response.json()["result"]["problems"]:
#     print(i)

# data = []
# for statistic in response.json()["result"]["problemStatistics"]:
#     # print(statistic["contestId"], statistic["index"])
#     for problem in response.json()["result"]["problems"]:
#         # print(problem)
#         if problem["contestId"] == statistic["contestId"] and problem["index"] == statistic["index"]:
#             problem["solvedCount"] = statistic["solvedCount"]
#             print(problem)
#             data.append(problem)

# print(response.json()["result"]["problemStatistics"])
# get_problems_data2 = codeforces_data.problemStatistics_data
# print(get_problems_data2)
# data_base.insert_data2("problemStatistics", get_problems_data2)
