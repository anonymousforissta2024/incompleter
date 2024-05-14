#Source: https://stackoverflow.com/questions/58815778/pytest-stop-runnig-with-attributeerror-module-html-has-no-attribute-td-in-p
from datetime import datetime
import html.parser
import pytest

@pytest.mark.optionalhook
def pytest_html_results_table_header(cells):
    cells.insert(2, html.th('Status_code'))
    cells.insert(1, html.th('Time', class_='sortable time', col='time'))
    cells.pop()

@pytest.mark.optionalhook
def pytest_html_results_table_row(report, cells):
    cells.insert(2, html.td(report.status_code))
    cells.insert(1, html.td(datetime.utcnow(), class_='col-time'))
    cells.pop()

@pytest.mark.hookwrapper
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()