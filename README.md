# Directory CLI

This project implements a Command Line Interface (CLI) for managing directories, providing essential operations to handle directory creation, deletion, movement, and listing.

## Overview

The CLI is built around two primary classes:

- **Node Class**: Represents a directory with a name and its child directories.
- **FileSystem Class**: Manages core directory operations, including creating, deleting, moving, and listing directories.

## Core Operations

### 1. **Create**  
   - Creates new directories, including handling nested paths.

### 2. **Delete**  
   - Removes directories and their contents recursively.

### 3. **Move**  
   - Relocates directories from one location to another.

### 4. **List Directories**  
   - Displays the current directory structure in a readable format.

## Helper Methods

- **_get_node**: Retrieves a directory node from a specified path.
- **_get_parent_and_name**: Obtains the parent node and name for a given path, useful for nested directory operations.

## Main Processing Flow

- Reads commands from standard input.
- Processes each command according to the specified functionality.
- Ensures output format strictly adheres to the given requirements.

## Usage

1. **Save the Code**  
   Save this implementation to a file, for example, `directory_cli.py`.

2. **Run the Program**  
   Execute the program from the command line:

   ```bash
   python directory_cli.py
   ```

3. **Enter Commands**  
   Input commands line by line. Once finished, end the input as follows:

   - Press `Ctrl+D` on Unix.
   - Press `Ctrl+Z` on Windows.

