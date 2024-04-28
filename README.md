# GoITNeo CS HW-05

## Task 1

Write a Python script that will read all files in the specified input folder (source folder) and distribute them to subfolders in the destination directory (output folder) based on the file extensions. The script should perform asynchronous sorting for more efficient handling of a large number of files.

### Step-by-step instructions
 - Import the required asynchronous libraries.
 - Create an `ArgumentParser` object for command-line argument processing.
 - Add necessary arguments for source and target folders.
 - Initialize asynchronous paths for source and target folders.
 - Write an asynchronous function `read_folder`, which recursively reads all files in the source folder and its subfolders.
 - Write an asynchronous function `copy_file`, which copies each file to the corresponding subfolder in the target folder based on its extension.
 - Set up error logging.
 - Launch the asynchronous function `read_folder` in the main block.

### Solution

The task is done in file `sort_files.py`. The file `seed_folder_files.py` cat be used to create fake files in the folder.

## Task 2