import os

def rename_files(directory):
    for filename in os.listdir(directory):
        if filename.startswith("0") and filename.endswith(".pdf"):
            new_filename = "TD" + filename[2:]
            os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))

# Specify the directory where the files are located
directory = "."

# Call the function to rename the files
rename_files(directory)
