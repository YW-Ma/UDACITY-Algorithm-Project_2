# SOLUTION
from os import listdir
from os.path import isfile, join

def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    # base case -- reach a file
    if isfile(path):
        return
    
    # reach a directory
    try:# make sure the path is existed.
        names = listdir(path)
    except Exception as error:
        print(error)
        return
    
    dirs = []
    # for the names in the path, check the type of it (can be file or dir)
    for name in names:
        # join the "name" with their "path" so as to use isfile function.
        full_name = join(path, name)
        if isfile(full_name):# is a file
            if full_name.endswith(suffix):# a file end with suffix
                print(full_name)
                
        else:# is not a file
            dirs.append(full_name)
    
    for full_name in dirs:# recursive call find_files on new directory
        find_files(suffix, full_name)
    return


# TEST
print("\n first test: ")
find_files(".c", ".")
"""
.\testdir\t1.c
.\testdir\subdir1\a.c
.\testdir\subdir3\subsubdir1\b.c
.\testdir\subdir5\a.c
"""
print("\n second test: ")
find_files(".h", ".")
"""
.\testdir\t1.h
.\testdir\subdir1\a.h
.\testdir\subdir3\subsubdir1\b.h
.\testdir\subdir5\a.h
"""

print("\n third test: ")
find_files(".c", ".\\testdir\\subdir6")
"""
This is invalid path, so the error should be:
[WinError 123]
"""

print("\n forth test: ")
find_files(".gitkeep", ".\\testdir\\subdir4")
"""
.\testdir\subdir4\.gitkeep
"""