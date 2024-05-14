#Source: https://stackoverflow.com/questions/69686855/python-throws-nonetype-error-when-trying-to-write-to-yaml-file
import os
import YAML

drives = ["A:\\", "B:\\", "C:\\", "D:\\", "E:\\", 
          "F:\\", "G:\\", "H:\\", "I:\\", "J:\\", "L:\\"]

for drive in drives:
    print("Searching in drive: " + f"'{drive}'")
    dir_path = drive
    for root, dirs, files in os.walk(dir_path):
        for file in files:

            # change the extension from '.mp3' to
            # the one of your choice.
            if file.endswith('.exe'):
                back = '\\'
                print("File path: " + f"'{root + back + str(file)}'")
                program = file
                path = root + back + str(file)

                with open('programs.yaml', 'r') as yaml_file:
                    cur_yaml = yaml.safe_load(yaml_file)
                    info = program + ": " + path
                    print("YAML data: " + f"'{info}'")
                    cur_yaml.append(info)
                    print("curyaml:" + cur_yaml)
                if cur_yaml:
                    with open('programs.yaml', 'w') as yaml_file:
                        yaml.safe_dump(cur_yaml, yaml_file)