#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
General File Utilities
'''

import os

__author__ = "Frank Pereny"
__copyright__ = "Copyright 2022, Frank Pereny"
__license__ = "GPL"
__version__ = "3"
__maintainer__ = "Frank Pereny"
__email__ = "fjpereny@gmail.com"
__status__ = "Production"


def os_separate(path):
    '''
    Sets a file path string to the correct separators based on the system OS.

        Parameters:
            path (str): The file path

        Returns:
            path (str): The file path with OS separators
    '''

    new_path = ""
    # Unix Systems (Linux, BSD, MacOS etc.)
    if os.sep == '/':
        new_path = path.replace('\\', '/')
    # Windows Systems
    if os.sep == '\\':
        new_path = path.replace('/', '\\')
    return new_path


def get_tree_file_size(path=".", extensions=None, recursive=True, symlinks=False):

    '''
    Returns the total file size within a directory.

        Parameters:
            path (str): The search directory
            extensions ([str]): Filter by a list of file extensions (e.g. ["txt", "jpeg"]).  Default None will yield all files.
            recursive (bool): Toggle to search sub-directories recursively.  Default True will include all sub-directories.
            symlinks (bool): Toggle to include linked (shortcut) files and directories. Default False will ignore symlinks.

        Returns:
            total (int): Total file size in bytes
    '''

    total = 0
    for entry in os.scandir(path):
        if entry.is_dir(follow_symlinks=symlinks):
            if recursive:
                try:
                    total += get_tree_file_count(entry.path, extensions)
                except PermissionError:
                    print("Permission Error: " + entry.path)
                except FileNotFoundError:
                    print("Directory Does Not Exist: " + entry.path)
        else:
            if extensions:
                for ext in extensions:
                    try:
                        if entry.name.endswith(ext):
                            total += entry.stat(follow_symlinks=symlinks).st_size
                            break
                    except PermissionError:
                        print("Permission Error: " + entry.path)
                    except FileNotFoundError:
                        print("Directory Does Not Exist: " + entry.path)
            else:
                total += entry.stat(follow_symlinks=symlinks).st_size
    return total


def get_tree_file_count(path, extensions=None, recursive=True, symlinks=False):

    '''
    Returns the total number files found within a directory.

        Parameters:
            path (str): The search directory
            extensions ([str]): Filter by a list of extensions.  Default None will yield all files.
            recursive (bool): Toggle to search sub-directories recursively.  Default True will include all sub-directories.
            symlinks (bool): Toggle to include linked (shortcut) files and directories. Default False will ignore symlinks.

        Returns:
            total (int): Integer total number of files found
    '''

    total = 0
    for entry in os.scandir(path):
        if entry.is_dir(follow_symlinks=symlinks):
            if recursive:
                try:
                    total += get_tree_file_count(entry.path, extensions)
                except PermissionError:
                    print("Permission Error: " + entry.path)
                except FileNotFoundError:
                    print("Directory Does Not Exist: " + entry.path)
        else:
            if extensions:
                for ext in extensions:
                    try:
                        if entry.name.endswith(ext):
                            total += 1
                            break
                    except PermissionError:
                        print("Permission Error: " + entry.path)
                    except FileNotFoundError:
                        print("Directory Does Not Exist: " + entry.path)
            else:
                total += 1
    return total

