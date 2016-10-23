Scripts to download comments from Youtube
=========================================

1. File Explanation
-------------------

  * README.md: 
    this document
  * client_secrets.json
    OAuth credentials created from Google API Console
  * youtube-v3-discoverydocument.json
    other authentication file
  * comments.py
    main script to download comments

2. How to run the code
----------------------

  *  install Google-api for your computer
   ```
    pip install --upgrade google-api-python-client
   ```
  * run (for example)
   ```
    python comments.py --videoid='m43UyujVsXk' --maxResults 20
   ```
