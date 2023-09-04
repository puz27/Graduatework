import requests


class RequestManager:
    """ """
    def __init__(self):
        self.__problems_data = []

    @property
    def problems_data(self) -> list:
        return self.__problems_data

    def get_request(self) -> None or str:
        """    """
        url_problemset = "https://codeforces.com/api/problemset.problems?tags=implementation"
        response = requests.get(url_problemset)
        if response.status_code == 200:
            if response.status_code == 200:
                for data in response.json()["result"]["problems"]:
                    self.__problems_data.append(data)
        else:
            return "Error:", response.status_code
