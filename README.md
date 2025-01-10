# Google Drive Folder Tools

## Overview

This repository contains two programs designed to manage and analyze Google Drive folders. These tools provide the ability to copy files and folder structures from one Google Drive folder to another and compare the contents of two folders to identify differences.

## Features

1. **File Copying**  
   - Copies files and folders from a source Google Drive folder to a destination folder.
   - Preserves the folder structure during the copy process.
   - Handles nested subfolders and supports Google Docs, Sheets, Slides, and other file types.

2. **Folder Diffing**  
   - Compares two Google Drive folders to detect differences in their contents.
   - Reports missing files or folders in the source or destination.
   - Supports recursive comparison for nested folder structures.

## Contents

This repository includes the following scripts:

1. **`copy_gdrive.py`**  
   - Authenticates with Google Drive.
   - Copies files and folder structures from a specified source folder to a destination folder.
   - Key Functions:
     - `copy_file`: Copies a single file to the destination folder.
     - `copy_folder_structure`: Creates a new folder in the destination and recursively copies the contents.
     - `move_folder_contents`: Handles copying files and subfolders.

2. **`diff_gdrive.py`**  
   - Authenticates with Google Drive.
   - Compares the contents of two folders and generates a detailed report of differences.
   - Key Functions:
     - `list_folder_contents`: Recursively lists the contents of a folder and organizes them into a dictionary structure.
     - `compare_folders`: Compares the folder dictionaries and identifies missing or extra files and folders.

## Requirements

These scripts are designed to be run in **Google Colab**, where you can easily authenticate and access your Google Drive. Follow these steps:

1. **Set up Google Colab:**
   - Open a Colab notebook at [Google Colab](https://colab.research.google.com/).
   - Upload the script you want to run (`copy_gdrive.py` or `diff_gdrive.py`).

2. **Install required libraries in Colab:**
   - Add the following line to the first cell of your Colab notebook:
     ```python
     !pip install --quiet --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
     ```

3. **Authenticate with Google Drive:**
   - Use the following in your notebook: (Copy_Gdrive)
     ```python
!pip install --quiet --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib

from google.colab import auth
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google.auth.transport.requests import Request
import io

# Authenticate and create the Drive API service
auth.authenticate_user()
drive_service = build('drive', 'v3')
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
   - Copy the content of the script into a cell and execute it, or reference the uploaded script directly.
   - Update the `source_folder_id` and `destination_folder_id` variables.

## Copyright & Licensing

Copyright (C) 2024 Talha Akhlaq <talhaakhlaq1@gmail.com>

Distributed under the MIT License. See LICENSE for details.
##

For more information on my projects and other academic work, please visit my [GitHub profile](https://github.com/TalhaAkhlaq).

