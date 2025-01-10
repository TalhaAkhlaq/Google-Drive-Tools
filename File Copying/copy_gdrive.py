def copy_file(file_id, destination_folder_id):
    try:
        # Get the file metadata
        file_metadata = drive_service.files().get(fileId=file_id, fields='name, mimeType').execute()

        # Copy the file metadata to the new location
        copied_metadata = {
            'name': file_metadata['name'],
            'parents': [destination_folder_id]
        }

        # Copy the file (Google Docs, Sheets, Slides, or any other file)
        drive_service.files().copy(fileId=file_id, body=copied_metadata).execute()
    except HttpError as error:
        print(f'An error occurred while copying the file: {error}')
        return None

def copy_folder_structure(source_folder_id, destination_folder_id):
    try:
        # Get the name of the source folder
        source_folder_metadata = drive_service.files().get(fileId=source_folder_id, fields='name').execute()
        source_folder_name = source_folder_metadata['name']

        # Create the source folder in the destination folder
        new_folder_metadata = {
            'name': source_folder_name,
            'mimeType': 'application/vnd.google-apps.folder',
            'parents': [destination_folder_id]
        }
        new_folder = drive_service.files().create(body=new_folder_metadata, fields='id').execute()

        # Copy the contents of the source folder into the newly created folder
        move_folder_contents(source_folder_id, new_folder['id'])
    except HttpError as error:
        print(f'An error occurred while copying the folder structure: {error}')
        return None

def move_folder_contents(source_folder_id, destination_folder_id):
    try:
        # List the contents of the source folder
        query = f"'{source_folder_id}' in parents and trashed = false"
        results = drive_service.files().list(q=query, fields='files(id, name, mimeType)').execute()
        items = results.get('files', [])

        for item in items:
            # Check if the item is a folder
            if item['mimeType'] == 'application/vnd.google-apps.folder':
                # Create a new folder in the destination with the same name
                folder_metadata = {
                    'name': item['name'],
                    'mimeType': 'application/vnd.google-apps.folder',
                    'parents': [destination_folder_id]
                }
                new_folder = drive_service.files().create(body=folder_metadata, fields='id').execute()

                # Recursively move the contents of the subfolder
                move_folder_contents(item['id'], new_folder['id'])
            else:
                # Copy the file to the destination folder
                copy_file(item['id'], destination_folder_id)
    except HttpError as error:
        print(f'An error occurred while moving folder contents: {error}')
        return None

# Replace these with your source and destination folder IDs
source_folder_id = 'Source'  # Source folder ID
destination_folder_id = 'Destination'  # Destination folder ID

# Copy the entire source folder into the destination folder
copy_folder_structure(source_folder_id, destination_folder_id)
print('Folder copied successfully.')
