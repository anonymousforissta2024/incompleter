#Source: https://stackoverflow.com/questions/67690534/filenotfounderror-when-using-shutil-copy
import shutil
destination_folder = "path_to_the_destination_folder"
source_file = "path_to_source_file\file1.pdf"
destination_file = "f{destination_folder}\any_random_folder_from_n_nested_folders\file1.pdf"
new_file= shutil.copy(source_file, destination_file )
print(new_file)