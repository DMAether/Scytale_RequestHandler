import requests
import extract

token = "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" #edit to match any PAT you will use
#repo = "repos/Scytale-exercise/Scytale_repo"
#repo = "/search/issues?q=repo:Scytale-exercise/Scytale_repo+is:pr+is:merged"
repo = "repos/Scytale-exercise/Scytale_repo/pulls?state=merged" #this option seems to give the best result

objExtract = extract.main(repo, token)

repoData = objExtract.request()


for item in repoData:
    print(item)

