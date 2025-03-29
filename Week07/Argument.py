# Reading text files
# This program reads in a text file and outputs the number of e's it contains, program should also take the filename from an argumnet on the command line
# Author: Michael Lawal
# Reference: Python file handling, command-line arguments, string methods.

import sys
import os

def count_es_in_file(filename):
    """Reads a text file and returns the count of 'e' characters (both 'e' and 'E')."""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            text = file.read()
            return text.lower().count('e')
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
        return None
    except IsADirectoryError:
        print(f"Error: The path '{filename}' is a directory, not a file.")
        return None
    except UnicodeDecodeError:
        print(f"Error: The file '{filename}' is not a valid text file (encoding issue).")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

def main():
    # Check if a filename argument is provided
    if len(sys.argv) != 2:
        print("Error: Please provide a filename as an argument.")
        sys.exit(1)

    filename = sys.argv[1]

    # Check if the file exists and is a text file
    if not os.path.isfile(filename):
        print(f"Error: The file '{filename}' does not exist or is not a valid file.")
        sys.exit(1)

    # Count occurrences of 'e' in the file
    count = count_es_in_file(filename)

    if count is not None:
        print(f"The file '{filename}' contains {count} occurrences of the letter 'e'.")

if __name__ == '__main__':
    main()
