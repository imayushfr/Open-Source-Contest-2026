from datetime import datetime
import os
import shutil
import sys

def print_usage():
    print("Usage: app <command> [arguments]")
    print("Commands: folders, files, list, pwd, cd, delete, rename, copy, move, info")

def create_folders(args):
    if not args:  # If no arguments are provided
        print("Error: Please provide folder name(s)")
        return
    
    for arg in args:
        try:
            if "," not in arg:
                os.mkdir(arg)
                print(f"Folder created: {arg}")
            else:
                # Different OS uses different path separators (\,/)
                path = arg.replace(",", os.sep)  
                # Don't crash if folder already exists
                os.makedirs(path, exist_ok=True) 
                print(f"Folder created: {path}")

        except FileExistsError:
            print(f"Error: Folder '{arg}' already exists.")

def create_files(args):
    if not args:
        print("Error: Please provide file name(s)")
        return
    
    for arg in args:
        try:
            # 'x' mode means exclusive, throws error if file already exists
            with open(arg, 'x'):
                pass
                print(f"File created: {arg}")
        
        except FileExistsError:
            print(f"Error: File '{arg}' already exists.")

def list_contents():
    try:
        # '.' for current working directory
        items = os.listdir('.')
        if not items:
            print("Empty Directory")
            return
        
        folders = []  # For printing folders first
        files = []    # Then files
        
        for item in items:
            if os.path.isdir(item):
                folders.append(item)
            else:
                files.append(item)
            
        for folder in folders:
            print(f"{folder}/")
        for file in files:
            print(file)

    except Exception as e:
        print(f"Error listing content: {e}")

def change_directory(args):
    if not args:
        print("Error: Please provide directory name")
        return
    try:
        os.chdir(args[0])
        print(f"Changed directory to: {os.getcwd()}")

    except FileNotFoundError:
        print(f"Error: Directory '{args[0]}' not found.")

def delete_items(args):
    if not args:
        print("Error: Please provide file or folder name(s)")
        return
    
    for arg in args:
        if not os.path.exists(arg):
            print(f"Error: '{arg}' does not exist.")
            continue

        try:
            if os.path.isdir(arg):  # If foldere
                shutil.rmtree(arg)  # Delete the whole tree
                print(f"Folder deleted: {arg}")
            else:
                os.remove(arg)
                print(f"File deleted: {arg}")

        except Exception as e:
            print(f"Error deleting '{arg}': {e}")

def rename_item(args):
    if len(args) != 2:
        print("Usage: app rename <old_name> <new_name>")
        return
    
    old_name = args[0]
    new_name = args[1]

    if not os.path.exists(old_name):
        print(f"Error: '{old_name}' does not exist.")
        return
    
    if os.path.exists(new_name):
        print(f"Warning: '{new_name}' already exists. Cannot overwrite it.")
        return
    
    try:
        os.rename(old_name, new_name)
        print(f"Renamed: '{old_name}' to '{new_name}'")

    except Exception as e:
        print(f"Error renaming '{old_name}': {e}")

def copy_item(args):
    if len(args) != 2:
        print("Usage: app copy <source> <destination>")
        return
    
    src = args[0]
    dst = args[1]

    if not os.path.exists(src):
        print(f"Error: Source '{src}' does not exist.")
        return
    
    if os.path.abspath(src) == os.path.abspath(dst):
        print(f"Error: Source and destination are same.")
        return
    
    try:
        if os.path.isdir(src):
            # Don't crash if folder already exists
            shutil.copytree(src, dst, dirs_exist_ok=True)
            print(f"Folder copied: '{src}' to '{dst}'")
        else:
            shutil.copy2(src, dst)
            print(f"File copied: '{src}' to '{dst}'")

    except Exception as e:
        print(f"Error copying '{src}': {e}")

def move_item(args):
    if len(args) != 2:
        print("Usage: app move <source> <destination>")
        return
    
    src = args[0]
    dst = args[1]

    if not os.path.exists(src):
        print(f"Error: Source '{src}' does not exist.")
        return
    
    if os.path.abspath(src) == os.path.abspath(dst):
        print(f"Error: Source and destination are same.")
        return
    
    try:
        shutil.move(src, dst)
        print(f"Moved: '{src}' to '{dst}'")
    except Exception as e:
        print(f"Error moving '{src}': {e}")

def folder_size(path):  # Calculating folder size using os.walk
    size = 0
    for dirpath, dirnames, filenames in os.walk(path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            if os.path.isfile(fp):
                size += os.path.getsize(fp)
    return size

def file_info(args):
    if not args:
        print("Error: Please provide a file or folder name")
        return
    
    if not os.path.exists(args[0]):
        print(f"Error: '{args[0]}' does not exist.")
        return
    
    try:
        stats = os.stat(args[0])

        if os.path.isdir(args[0]):
            size_kb = round(folder_size(args[0]) / 1024, 2)
        else:
            size_kb = round(stats.st_size / 1024, 2)

        # The st.ctime property is deprecated. Alternative is st.birthtime. 
        # But st.ctime is used here because st.birthtime doesn't exist in Linux.
        created = datetime.fromtimestamp(stats.st_ctime).strftime('%Y-%m-%d %H:%M:%S')
        modified = datetime.fromtimestamp(stats.st_mtime).strftime('%Y-%m-%d %H:%M:%S')
        accessed = datetime.fromtimestamp(stats.st_atime).strftime('%Y-%m-%d %H:%M:%S')

        absolute_path = os.path.abspath(args[0])

        print(f"\n--- Information for {args[0]} ---")
        print(f"Path- {absolute_path}")
        print(f"Size: {size_kb} KB")
        print(f"Created: {created}")
        print(f"Modified: {modified}")
        print(f"Accessed: {accessed}")

    except Exception as e:
        print(f"Error retrieving info for '{args[0]}': {e}")

def main():
    # If not enough arguments are provided
    if len(sys.argv) < 2: 
        print_usage()
        sys.exit(1)

    command = sys.argv[1].lower()
    args = sys.argv[2:]

    commands = {
        "folders": create_folders,
        "files": create_files,
        "cd": change_directory,
        "delete": delete_items,
        "rename": rename_item,
        "copy": copy_item,
        "move": move_item,
        "info": file_info
    }

    if command in commands:
        commands[command](args)
    elif command == "list":
        list_contents()
    elif command == "pwd":
        print(os.getcwd())

    else:
        print(f"Error: Unknown command '{command}'")
        print_usage()

if __name__ == "__main__":
    main()

