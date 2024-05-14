#Source: https://stackoverflow.com/questions/54575267/typeerror-for-datefield-django-xlwt-library
import xlwt

from django.http import HttpResponse
from django.contrib.auth.models import User

def GenerateCompanyCSV(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="users.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Users')

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Company Name', 'Company Email', 'Count of people','Created Date', 'Current Monthly Payment', 'Is TABopts Customer', 'Status', ]

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = Company.objects.exclude(id=1).exclude(
                    company_is_deleted=True
                ).annotate(
                    number_of_company_users=Count('userprofile')
                ).values_list(
                    'company_name', 
                    'company_email', 
                    'number_of_company_users',
                    'company_created',
                    'company_monthly_payment', 
                    'company_tab_opts',
                    'company_status',

                )
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response