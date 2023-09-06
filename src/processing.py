from request_manager import RequestManager
from data_base_manager import DBManager
from utils import config


# work with base
connection_params = config()
data_base = DBManager(connection_params, "codeforces_base")
data_base.create_database("codeforces_base")
data_base.create_tables()


# work with requests
codeforces_data = RequestManager()
codeforces_data.get_request()
get_problems_data = codeforces_data.problems_data
# zzz = [555, 'A', 'Winner', None, 1500, ['hashing', 'implementation'], 'PROGRAMMING'], [1, 'B', 'Spreadsheet', None, 1600, ['implementation', 'math'], 'PROGRAMMING']
data_base.insert_data("problems", get_problems_data)

