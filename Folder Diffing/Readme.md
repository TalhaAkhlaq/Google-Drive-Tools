# Folder Diffing

## Overview

The script is designed to be run in **Google Colab**, where you can easily authenticate and access your Google Drive. Follow these steps:

1. **Set up Google Colab:**
   - Open a Colab notebook at [Google Colab](https://colab.research.google.com/).
   - Upload the script you want to run (`copy_gdrive.py` or `diff_gdrive.py`).

2. **Install required libraries in Colab:**

3. **Add the following to the first cell of your Colab notebook:**
     ```python
     # Install the necessary libraries
     !pip install --quiet --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib

   from google.colab import auth
   from googleapiclient.discovery import build
   from googleapiclient.errors import HttpError

   # Authenticate and create the Drive API service
   auth.authenticate_user()
   drive_service = build('drive', 'v3')
     ```
4. **Run the script:**
   - Add `copy_gdrive.py` to the second cell of your Colab notebook.
   - Update the `source_folder_id` and `destination_folder_id` variables.
  
