import requests
import extract

token = "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"
repo = "repos/Scytale-exercise/scytale-repo3"

objExtract = extract.main(repo, token)

objExtract.request()