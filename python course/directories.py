from pathlib import Path

# Absolute path - from the root of the hard disk
# c:\Program Files\Microsoft

# Relative path - Path() -> from the current file OR Path('ecommerce') give the name of it like 'ecommerce'

path = Path()

# print(path.exists())

# create a directory
# print(path.mkdir())

# remove a directory
# print(path.rmdir())

# glob() -> search for files and directories
# the arguments will define a search pattern
# '*' -> everything, all files and directories
# '*.*' -> we'll only get the files in the current directory, but not the directories

for file in path.glob('*'):
    print(file)
