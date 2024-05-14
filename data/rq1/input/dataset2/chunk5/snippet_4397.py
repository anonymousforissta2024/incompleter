#Source: https://stackoverflow.com/questions/55667502/attributeerror-int-object-has-no-attribute-squeeze
def make_dashboard(x, gdp_change, unemployment, title, file_name):
    output_file(file_name)
    p = figure(title=title, x_axis_label='year', y_axis_label='%')
    p.line(x.squeeze(), gdp_change.squeeze(), color="firebrick", line_width=4, legend="% GDP change")
    p.line(x.squeeze(), unemployment.squeeze(), line_width=4, legend="% unemployed")
    show(p)


make_dashboard(x=1948, gdp_change=10, unemployment=3.75, title=title, file_name=file_name)