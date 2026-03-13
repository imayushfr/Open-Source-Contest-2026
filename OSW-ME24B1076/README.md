# File Management CLI System written in Python

## Folder Structure

```text
OSW-ME24B1076/
├── app.py         
├── app.bat         
├── README.md       
├── LICENSE 
└── .gitignore
```
## Language Used
### Python 3

## Libraries Used
### os, sys, shutil, datetime

## Feature Description

| Feature                | Description                                         | Syntax                               |
| ---------------------- | --------------------------------------------------- | ------------------------------------ |
| Create folders         | Create one or more folders in the current directory | `app folders <name1> <name2> ...`  |
| Create nested folders  | Create folders inside existing folders              | `app folders <parent>,<child>`     |
| Create files           | Create one or more files                            | `app files <name1> <name2> ...`    |
| List contents          | Display files and folders in the current directory  | `app list`                         |
| Show current directory | Display the current working directory               | `app pwd`                          |
| Change directory       | Move to another directory                           | `app cd <folder>`                  |
| Delete files/folders   | Remove files or folders                             | `app delete <name>`                |
| Rename files/folders   | Rename a file or folder                             | `app rename <old_name> <new_name>` |
| Copy files             | Copy a file to another location                     | `app copy <source> <destination>`  |
| Move files             | Move a file or folder to another location           | `app move <source> <destination>`  |
| Show file details      | Display metadata such as size and creation date     | `app info <file>`                  |

- Error handling and clear error messages are provided.
- SOLID principles, human-readable, white spaces and clean code practices are followed as much as possible.


## Dependencies

### Python 3.x. 
### No external dependencies

## How to run on your local machine

1. Make sure Python 3 is  installed on your system.

2. Clone this repository into your local machine using ```git clone```.

3. Open your terminal/CMD and navigate to this cloned repo/folder.

## How to use

### For Windows Users: 
```app.bat``` file is provided, so one can execute commands directly like :

```app folders <name1> <name2>```

Instead of :

```python app.py folders <name1> <name2>```

Although both commands works for windows.

### For Linux/Mac Users:

You can run the program using :

```python app.py folders <name1> <name2>```

Although you can make your own alias as :

```alias app="python3 app.py"```

## Important Note

- In ```file_info()``` function's ```created``` variable, the ```st.ctime``` property is deprecated. Alternative is ```st.birthtime```. 

- But ```st.ctime``` is used here because ```st.birthtime``` doesn't exist in Linux.

## Limitation
- ```change_directory()``` function do not truly change the directory.

## Future Enhancements
- ```change_directory()``` function will work as intended.
-  Refactoring code into multiple modular files and folders.
