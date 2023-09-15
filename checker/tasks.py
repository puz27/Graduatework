from checker.celery import app
from src.data_base_manager import DBManager
from src.request_manager import RequestManager
from src.utils import config


codeforces_data = RequestManager("https://codeforces.com/api/problemset.problems")
connection_params = config("postgresql")
data_base = DBManager(connection_params, "codeforces_base")


@app.task
def check():
    print('Update base.')
    codeforces_data.get_request()
    get_problems_data = codeforces_data.problems_data
    for problem in get_problems_data:
        data_base.insert_new_data("problems", problem)

