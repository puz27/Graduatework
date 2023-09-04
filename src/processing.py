from request_manager import RequestManager
from data_base_manager import DBManager
from utils import config
#
# codeforces_data = RequestManager()
# codeforces_data.get_request()
# print(codeforces_data.problems_data)

connection_params = config()
data_base = DBManager(connection_params, "codeforces_base")
# data_base.create_database("codeforces_base")
data_base.create_tables()
