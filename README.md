# PythonMagic 

Unleash the power of Python with a curated collection of magical scripts to simplify your computer usage and coding workflows. I personally use these for data processing and Machine Learning workflows in my Data Science projects.

## What Python Offers:

- **Effortless Automation:** These scripts were made for seamless automation of routines.
- **Tailoring:** Customize them to make new Python programs that suit your specific needs.

## List of Scripts:

1. ### `searchify.py`

   The `searchify.py` script transforms your search terms which could be corrupted with spaces and special characters etc into Google search URLs for easy checking, making it faster to search from a long list of terms in a database instead of having to do it individually through copy pasting etc.

   #### Usage:

   Replace `terms_list` variable, executing the script will then generate Google search URLs for the given list of terms in `term_list`, handling special characters, leading or trailing spaces, and converting spaces to `+` in the URL turning it into valid Google search URLs that are clickable.

   ```bash
     python searchify.py
   ```
   #### Sample Output:
   ```
    https://www.google.com/search?q=Ma+ch+n3+Learn+ng
    https://www.google.com/search?q=Cry+pt0graphy+2020
    https://www.google.com/search?q=Quantum+Computing
    https://www.google.com/search?q=Deep+Learn+ng
    https://www.google.com/search?q=Pyth+on+Coding
    https://www.google.com/search?q=Space+Exploration
    https://www.google.com/search?q=V1rtu+l+R3al1ty
    https://www.google.com/search?q=Blockchain+Technology

   ```

2. ### `folder_magic.py`

   The `folder_magic.py` script adds a specified text to the names of all folders in a given directory and then invokes an external program with the modified folder names with flags, useful when you want to extract and perform some random operation on folder names.

   #### Usage:

   Replace `'\path\to\folder'` with the actual path of the folder you want to process and `program_path` with the program you want the names to run on. Adjust the `text_to_add` variable with the text you want to append to each folder name. Also add any suitable flags that the program accepts by changing `-some-flag` in `command` variable. 

   ```bash
     python folder_magic.py
   ```

3. ### `low_resolution_videos.py`

   The `low_resolution_videos.py` script swiftly scans through all video files in a specified folder and its subfolders, identifying those with resolutions lower than certain threshold (240p). The script is useful when you want to exclude low resolution videos from your training or test set when working with computer vision models.

   #### Usage:

   Replace `'\path\to\folder'` with the actual path of the folder you want to process.

   ```bash
     python low_resolution_videos.py
   ```



## Contribution:

Feel free to add your own spells to PythonMagic.

## Other magical repositories:

- [**AHKMagic**](https://github.com/himanshuxd/AHKMagic) - Automate Windows tasks with AutoHotKey scripts.
- [**BatchMagic**](https://github.com/himanshuxd/BatchMagic) - Your go-to source for efficient Windows batch scripts.