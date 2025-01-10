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

## Copyright & Licensing

Copyright (C) 2024 Talha Akhlaq <talhaakhlaq1@gmail.com>

Distributed under the MIT License. See LICENSE for details.
##

For more information on my projects and other academic work, please visit my [GitHub profile](https://github.com/TalhaAkhlaq).

