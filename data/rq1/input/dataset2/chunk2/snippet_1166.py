#Source: https://stackoverflow.com/questions/71753625/python-subprocess-call-file-not-found-error
import minecraft_launcher_lib
import subprocess

minecraft_directory = "C:\\Users\\Mert KAPLANDAR\\AppData\\Roaming\\.minecraft"

options = minecraft_launcher_lib.utils.generate_test_options()

minecraft_command = minecraft_launcher_lib.command.get_minecraft_command("1.8.9", minecraft_directory, options)

subprocess.call(minecraft_command)