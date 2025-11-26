# Scytale_RequestHandler
The completed assignmnet for Scytale. A python program that retrieves Pull requests from the Scytale Git Repository using the GitHub API

Please Follow the following steps for using the project:
Edit the transform.py script as follows:
  At line 6, change the token variable to your own GitHub API token, as the one there by default will no longer be available.

  For filtering:
    At line 102, change the filterField variable to whichever of the following fields you wish to filter; 'PR Number', 'PR title', 'Author', 'Merge Date', 'CR_Passed', 'CHECKS_PASSED'.
    At line 103, change the filterValue field to whicher value you wish to filter for from your chosen field.

When ready to execute, run the transform.py script

-------------------------------------------------------
After completion, the following subfolders and files will be created in the current directory of the executed script:
  raw folder:
    rawAPI.json: contains the raw response from the initial request to the API
  csv Folder:
    unfiltered.csv; contains the results prior to filtering
    filtered.csv; contains the filtered results
    
