import requests
from utils import prepare_problem_format, prepare_problem_format2


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

                # for data in response.json()["result"]["problems"]:
                #     prepared_data = prepare_problem_format(data)
                #     self.__problems_data.append(prepared_data)

                # for data in response.json()["result"]["problemStatistics"]:
                #     prepared_problemStatistics_data = prepare_problem_format2(data)
                #     self.__problemStatistics_data.append(prepared_problemStatistics_data)

                for statistic in response.json()["result"]["problemStatistics"]:
                    # print(statistic["contestId"], statistic["index"])
                    for problem in response.json()["result"]["problems"]:
                        # print(problem)
                        if problem["contestId"] == statistic["contestId"] and problem["index"] == statistic["index"]:
                            problem["solvedCount"] = statistic["solvedCount"]
                            prepared_data = prepare_problem_format(problem)
                            self.__problems_data.append(prepared_data)
        else:
            return "Error:", response.status_code
