import os
import subprocess

def process_folders(folder_path, text_to_add, program_path):
    # Get a list of all folder names in the specified directory
    folder_names = [folder for folder in os.listdir(folder_path) if os.path.isdir(os.path.join(folder_path, folder))]

    # Iterate through each folder
    for folder_name in folder_names:
        # Create the modified folder name by adding the provided text
        modified_folder_name = folder_name + text_to_add

        # Build the command to run the external program with the given flag
        command = f'"{program_path}" -s "{modified_folder_name}" -some-flag'

        # Use subprocess to run the command
        subprocess.run(command, shell=True)

if __name__ == "__main__":
    # Specify the folder path, text to add, and program path
    folder_path = '\path\to\folder'
    text_to_add = ' magic'
    program_path = r'C:\Program Files\Some Folder\Some Program.exe'

    # Call the function to process folders
    process_folders(folder_path, text_to_add, program_path)
