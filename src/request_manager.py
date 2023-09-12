import requests
from src.utils import prepare_problem_format


class RequestManager:
    """ """
    def __init__(self):
        self.__problems_data = []
        # self.__problemStatistics_data = []

    @property
    def problems_data(self) -> list:
        return self.__problems_data

    # @property
    # def problemStatistics_data(self) -> list:
    #     return self.__problemStatistics_data

    def get_request(self) -> None or str:
        """    """
        url_problemset = "https://codeforces.com/api/problemset.problems"
        response = requests.get(url_problemset)
        if response.status_code == 200:
            if response.status_code == 200:
                self.__problems_data.clear()

                for statistic in response.json()["result"]["problemStatistics"]:
                    for problem in response.json()["result"]["problems"]:
                        # print(problem)
                        if problem["contestId"] == statistic["contestId"] and problem["index"] == statistic["index"]:
                            problem["solvedCount"] = statistic["solvedCount"]
                            prepared_data = prepare_problem_format(problem)
                            print(prepared_data)
                            self.__problems_data.append(prepared_data)
        else:
            return "Error:", response.status_code
