#Source: https://stackoverflow.com/questions/55582245/subprocess-doesnt-find-my-file-file-not-found-error
import subprocess as sb
current_path = os.path.realpath(__file__)
sb.call(['python3', current_path])