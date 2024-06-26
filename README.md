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

The task is done in file `sort_files.py`. The file `seed_folder_files.py` can be used to generate fake files in the folder.

## Task 2
Write a Python script that downloads text from a given URL, analyzes the frequency of words in the text using MapReduce and visualizes the top words with the highest frequency in the text.

### Step-by-step instructions
1. Import the necessary modules (`matplotlib` and others).
2. Get the code implementation of MapReduce from the lecture notes.
3. Create a function `visualize_top_words` for visualizing the results.
4. In the main block of code retrieve the text from the URL, apply MapReduce and visualize the results.

### Solution

The task is done in file `top_words.py`.
