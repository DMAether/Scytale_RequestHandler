import requests #for comunicatiting with the api over http

#class that is used by transform.py
#variables for the path to the repo and the access token are recieved by transform.py when initialized
class main():
    def __init__(self, repo, token):
        self.baseUrl = "https://api.github.com/"
        self.repo = repo
        self.token = token

    #connect to api and get repo information
    def request(self):
        url = f"{self.baseUrl}{self.repo}"
        response = requests.get(url)
        #if response returns code 200, then the request was succesful
        #check if it was successful
        if response.status_code == 200:
            print("ok")
        else:
            print(f"Error in request, code: {response.status_code}")    
