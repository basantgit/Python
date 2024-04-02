import os

def list_file_in_folder(folder_path):
    try:
        files = os.listdir(folder_path)
        return files, None
    except FileNotFoundError:
        return None, 'folder not found'
    except PermissionError:
        return None, 'Dont have much permissions for acces the folder'
    
def main():
    folder_paths = input("Please enter folder name with the space: ").split()
    for folder_path in folder_paths:
        files, error_messages = list_file_in_folder(folder_path)
        if files:
            print(f"files in {folder_path}")
            for file in files:
                print(file)
    else:
        print(f"error in {folder_path}: {error_messages}")

if __name__ == "__main__":
    main()
