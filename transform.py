import requests
import extract
import os.path
import csv

token = "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" #edit to match any PAT you will use
repo = "Scytale-exercise/Scytale_repo" #change this to the owner and name of the repo you want
#repo = "microsoft/agent-lightning" #used for testing

#checks whether or not there is at least 1 passed review for each pull request
def checkStateReviews(reviews):
    for review in reviews: #loops until it finds an approved review and returns true, if not found by end, returns False

        #print(f"{review["state"]}")

        if f"{review["state"]}" == "APPROVED" :
            return True
        
    return False

def checkCodeState(statuses):
    for status in statuses:
        print(f"{status["state"]}")
        if not f"{status["state"]}" == "success":
            return False
    return True    

#write final output to CSV file under CSV folder
def writeCSV(csvData, filter):
    fileName = "unfiltered.csv"
    if filter:
        fileName = "filtered.csv"
    curDir = os.path.dirname(os.path.abspath(__file__))
    csvFolder = os.path.join(curDir, 'csv')
    if not os.path.exists(csvFolder):
        os.mkdir(csvFolder)

    with open(os.path.join(csvFolder, fileName), 'w', newline='') as csvfile:
        fieldnames = ['PR Number', 'PR title', 'Author', 'Merge Date', 'CR_Passed', 'CHECKS_PASSED']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(csvData)
    print("[Info] CSV File created succesfully")    

objExtract = extract.main(token)
repoData = objExtract.request(f"repos/{repo}/pulls?state=merged", False) #fetch raw json from api

csvData = [] #prepare empty csv list to append during loops

#loop for each item in raw

for item in repoData:
    print("-----------------------------\nnewMerged Pull Request")
    number = f"{item["number"]}"
    print(number)
    title = f"{item["title"]}"
    print(title)
    author = f"{item["user"]['login']}"
    print(author)
    mergeDate = f"{item["merged_at"]}"
    print(mergeDate)

    #we need to check if the current pull request was reviewed or not, and get the reviews if so
    reviewData = objExtract.request(f"repos/{repo}/pulls/{number}/reviews", True)
    
    CR_Passed = False #defualt, if the if statement comes back false, it will remain as False test
    if reviewData:
        print("Reviewed")
        #get boolean for CR_Passed
        CR_Passed = checkStateReviews(reviewData)
        if CR_Passed:
            print("This pull request is approved")
        else:
            print("No applicable reviews found")
    else:
        print("not reviewed")

    #test checks
    #to get the statuses, we first need to find the sha code from "item"
    sha = f"{item["base"]["sha"]}"
    statusData = objExtract.request(f"repos/{repo}/commits/{sha}/statuses", True)
    
    #if the returned statusData is empty, then it means that we must set it to Failed
    CHECKS_PASSED = False
    if statusData:
        CHECKS_PASSED = checkCodeState(statusData)
        if(CHECKS_PASSED):
            print("All check passed")
        else: 
            print("One or more tests were not marked as succesfull")
    else:
        print("No Status Found")
        
    #append to csv
    tempStore = {'PR Number': number, 'PR title': title, 'Author': author, 'Merge Date': mergeDate, 
                 'CR_Passed': CR_Passed, 'CHECKS_PASSED': CHECKS_PASSED}
    csvData.append(tempStore)

#print(csvData)

#filtering
filterField = "Author" #enter exact fieldname for filtering field
filterValue = "aviyashar" #enter exact value of chosen field to filter for
csvDataFiltered = []
#loop through every item and add those that match the filter to csvDataFiltered
for item in csvData:
    if  f"{item[f"{filterField}"]}" == filterValue:
        csvDataFiltered.append(item)
    

if repoData:   
    writeCSV(csvData, False) #unfiltered output
    writeCSV(csvDataFiltered, True) #filtered output