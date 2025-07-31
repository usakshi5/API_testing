import config
import requests


def request_method(url, json = None, headers = None, method=None):
    if method =='GET':
        response = requests.get(url, headers= headers)
    elif method == 'POST':
        response = ''
    else: response = ''
    return response


class GitHubClient:
    uri = 'https://api.github.com/'
    auth = {'Authorization': f"Bearer {config.bearer_token}"}
    # def __init__(self):
    #     a = 'auth'

    def get_user_auth(self):
        url = self.uri + 'user'
        return request_method(url, headers = self.auth, method='GET')

    def get_user_repos(self):
        url = self.uri+'user/repos'
        return request_method(url, headers = self.auth, method='GET')