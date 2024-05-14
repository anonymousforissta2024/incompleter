#Source: https://stackoverflow.com/questions/71196458/python-3-10-filenotfounderror-existing-path-with-unicode-characters
for root, _, filenames in os.walk(maybe_dir):
    for file in filenames:
        # Prepare relative paths:
        relative_dir = os.path.relpath(root, maybe_dir)
        relative_file = os.path.join(relative_dir, file)

        # Get unique filename:
        unique_filename = uuid.uuid4().hex
        unique_filename_with_ext = unique_filename + file_extension
        new_path_and_filename = os.path.join(
            full_output_path, unique_filename_with_ext
        )

        current_file = os.path.abspath(os.path.join(root, file))

        # Copying files:
        shutil.copy(current_file, new_path_and_filename)