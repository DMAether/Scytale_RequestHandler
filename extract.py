import requests #for comunicatiting with the api over http
import os.path
import json

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
        #pack token into packet to be sent in request as the header
        headers = {'Authorization': 'token ' + self.token}
        response = requests.get(url, headers=headers)
        #if response returns code 200, then the request was succesful
        #check if it was successful
        if response.status_code == 200:
            print("[Info] Repo retrieved successfuly")
            #transform to json format then send back to transform.py
            repoData = response.json()
            main.writeJson(repoData)
            return repoData
        else:
            print(f"[Error] Error in request, code: {response.status_code}")
            return    
        
    #write the raw output from api to json file under "Raw" folder in current directory    
    def writeJson(repoData):
        #get the current directory, based on where the script running is from
        curDir = os.path.dirname(os.path.abspath(__file__))

        #all raw outputs will go under a "raw" folder
        #first check if the folders already exist, otherwise, we make them
        rawFolder = os.path.join(curDir, 'raw')
        if not os.path.exists(rawFolder):
            os.mkdir(rawFolder)

        #create raw json and raw folder
        with open(os.path.join(rawFolder, 'rawAPI.json'), 'w', encoding='utf-8') as f:
            json.dump(repoData, f, ensure_ascii=False, indent=4)
