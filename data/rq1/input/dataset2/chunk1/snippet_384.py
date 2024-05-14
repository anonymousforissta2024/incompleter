#Source: https://stackoverflow.com/questions/75634860/problem-with-sdv-library-in-python-nameerror-name-load-tabular-demo-is-not-d
from sdv.demo import get_available_demos
demos = get_available_demos()
data = load_tabular_demo('student_placements')