#Source: https://stackoverflow.com/questions/62406132/django-2-0-13-2-1-upgrade-causes-std-library-function-to-not-find-module-att
import os
import sys

if __name__ == "__main__":
    package_dir = os.path.dirname(os.path.abspath(__file__))
    sys.path.remove(package_dir)
    sys.path.insert(0, os.path.normpath(os.path.join(package_dir, '..')))
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)