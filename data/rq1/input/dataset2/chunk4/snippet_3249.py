#Source: https://stackoverflow.com/questions/65307806/attributeerror-shiftchangefilter-object-has-no-attribute-values-list
from django.utils import timezone
now_aware = timezone.now()
import xlwt,openpyxl
def exportgenesys_data(request):
    allgenesys = ShiftChange.objects.all()
    genesys_filter = ShiftChangeFilter(request.GET,queryset=allgenesys )
    print('download:',genesys_filter.qs)

    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="Genesys_ShiftTiming.xls"'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('GenesysShiftChange Data')  # this will make a sheet named Users Data
    # Sheet header, first row
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True
    columns = ['id', 'ConnectID', 'Shift_timing', 'EmailID', 'Vendor_Company', 'Project_name', 'SerialNumber',
               'Reason', 'last_updated_time']
    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)  # at 0 row 0 column
    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()
    rows = genesys_filter.values_list('id', 'ConnectID', 'Shift_timing',
                           'EmailID', 'Vendor_Company', 'Project_name',
                           'SerialNumber', 'Reason', 'last_updated_time')


    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)
    wb.save(response)
    return response