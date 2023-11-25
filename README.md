# PythonMagic 

Unleash the power of Python with a curated collection of magical scripts to simplify your computer usage and coding workflows. I personally use these for data processing and Machine Learning workflows in my Data Science projects.

## What PythonMagic Offers:

- **Effortless Automation:** Elevate your computer experience with scripts designed for seamless automation of routines.
- **Versatile Spells:** Explore scripts suitable for both Python beginners and wizards of code.
- **Tailored Potions:** Customize and adapt scripts to concoct solutions that suit your specific productivity needs.

## List of Scripts:

1. ### `searchify.py`

   The `searchify.py` script transforms your search terms which could be corrupted with spaces and special characters etc into Google search URLs for easy verification and checking, making it easier to search from a long list of terms from a database instead of having to copy paste each term.

   #### Usage:

   Simply run the script, and it will generate Google search URLs for a list of terms, handling special characters, leading/trailing spaces, and converting spaces to `+` in the URL turning them into valid Google search URLs that are clickable.

   ```bash
     python searchify.py
   ```
   #### Sample Output :
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
## Contribution :

Feel free to contribute your own spells to PythonMagic. Let Python empower us to create, automate, and do more.

## Other magical repositories:

- [**AHKMagic**](https://github.com/himanshuxd/AHKMagic) - Automate Windows tasks with AutoHotKey scripts.
- [**BatchMagic**](https://github.com/himanshuxd/BatchMagic) - Your go-to source for efficient Windows batch scripts.