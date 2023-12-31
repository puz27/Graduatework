import requests
from src.utils import prepare_problem_format


class RequestManager:
    """ Class work with remote site and grab data from it. """
    def __init__(self, url_problemset):
        self.__url_problemset = url_problemset
        self.__problems_data = []

    @property
    def problems_data(self) -> list:
        return self.__problems_data

    def get_request(self) -> None or str:
        """ Make request to api. Prepare data and save to problems_data list. """
        try:
            response = requests.get(self.__url_problemset)
            if response.status_code == 200:
                self.__problems_data.clear()
                print("Waiting...")
                for statistic in response.json()["result"]["problemStatistics"]:
                    for problem in response.json()["result"]["problems"]:
                        if problem["contestId"] == statistic["contestId"] and problem["index"] == statistic["index"]:
                            problem["solvedCount"] = statistic["solvedCount"]
                            prepared_data = prepare_problem_format(problem)
                            self.__problems_data.append(prepared_data)
        except Exception as er:
            print(er)
