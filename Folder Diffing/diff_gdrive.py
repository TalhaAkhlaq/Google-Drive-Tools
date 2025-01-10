def list_folder_contents(folder_id):
    try:
        items_dict = {}

        # List the contents of the folder
        query = f"'{folder_id}' in parents and trashed = false"
        results = drive_service.files().list(q=query, fields='files(id, name, mimeType)').execute()
        items = results.get('files', [])

        for item in items:
            if item['mimeType'] == 'application/vnd.google-apps.folder':
                # If the item is a folder, recursively list its contents
                items_dict[item['name']] = list_folder_contents(item['id'])
            else:
                # If it's a file, add it to the dictionary
                items_dict[item['name']] = 'file'

        return items_dict
    except HttpError as error:
        print(f'An error occurred: {error}')
        return None

def compare_folders(source_dict, destination_dict, parent_path=''):
    differences = []

    # Check for items in source that are not in destination
    for item in source_dict:
        if item not in destination_dict:
            # Missing in destination
            differences.append({
                'status': 'missing_in_destination',
                'item': item,
                'present_in': f'source at {parent_path}/{item}',
                'missing_in': f'destination, should be at {parent_path}/{item}'
            })
        elif isinstance(source_dict[item], dict):
            # If the item is a subfolder, compare recursively
            sub_diffs = compare_folders(source_dict[item], destination_dict[item], parent_path + '/' + item)
            differences.extend(sub_diffs)

    # Check for items in destination that are not in source
    for item in destination_dict:
        if item not in source_dict:
            # Missing in source
            differences.append({
                'status': 'missing_in_source',
                'item': item,
                'present_in': f'destination at {parent_path}/{item}',
                'missing_in': f'source, should be at {parent_path}/{item}'
            })

    return differences

# Replace these with your source and destination folder IDs
source_folder_id = 'source'  # Source folder ID
destination_folder_id = 'destination'  # Destination folder ID

# List contents of both folders
source_contents = list_folder_contents(source_folder_id)
destination_contents = list_folder_contents(destination_folder_id)

# Compare the folder contents
differences = compare_folders(source_contents, destination_contents)

if not differences:
    print('The folders are identical.')
else:
    print('Differences found:')
    for diff in differences:
        if diff['status'] == 'missing_in_destination':
            print(f"Item '{diff['item']}' is present in the source folder at {diff['present_in']}")
            print(f"  - It is missing in the destination folder. It should be at {diff['missing_in']}\n")
        elif diff['status'] == 'missing_in_source':
            print(f"Item '{diff['item']}' is present in the destination folder at {diff['present_in']}")
            print(f"  - It is missing in the source folder. It should be at {diff['missing_in']}\n")
