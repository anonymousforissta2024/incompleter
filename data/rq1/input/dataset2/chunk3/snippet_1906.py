#Source: https://stackoverflow.com/questions/70685618/copying-files-with-concurrent-futures-raising-attributeerror-silently
def download_files(directories: set, path_tuples: set) -> os.path:
    """Copies the files"""
    def copy_file(_path_tuple: tuple):
        from_path, to_path = _path_tuple
        try:
            shutil.copy(from_path, to_path)
            return to_path

        except PermissionError:
            print(f"Tried to copy file from {from_path} to {to_path}, but was denied access")
        
        except FileNotFoundError:
            print(f"Tried to copy file from {from_path} to {to_path}, but invalid path!")

    print(f"Found {len(path_tuples)} files to copy, in {len(directories)}")

    for directory in directories:
        if not os.path.exists(directory):
            print(f"Local directory didn't exist, create it")
            try:
                os.mkdir(directory)
            except PermissionError:
                print(f"Tried to make folder at {directory}, but was denied access")
            except FileNotFoundError:
                print(f"Tried to make folder at {directory}, but invalid path!")
                
    if path_tuples:
        
        # with concurrent.futures.ProcessPoolExecutor() as executor:
        #     results = {executor.submit(copy_file, path_tuple) for path_tuple in path_tuples}
        #
        #     for target_path in concurrent.futures.as_completed(results):
        #         print(f"Done copying file {target_path}")
        
        for path_tuple in path_tuples:
            copy_file(path_tuple)