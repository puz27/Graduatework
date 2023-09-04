from request_manager import RequestManager

codeforces_data = RequestManager()
codeforces_data.get_request()
print(codeforces_data.problems_data)
