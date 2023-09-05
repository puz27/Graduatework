from request_manager import RequestManager
from data_base_manager import DBManager
from utils import config





# work with base
connection_params = config()
data_base = DBManager(connection_params, "codeforces_base")
# data_base.create_database("codeforces_base")
# data_base.create_tables()


# work with requests
codeforces_data = RequestManager()
codeforces_data.get_request()
for problem in codeforces_data.problems_data:
    print(problem)


# data_base.insert_data("codeforces_base", codeforces_data.problems_data)

