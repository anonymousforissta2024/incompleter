#Source: https://stackoverflow.com/questions/37220843/attributeerror-str-object-has-no-attribute-day-error-when-trying-to-put-day
data = {'days': [],
        'times': []}

with open(open_file) as in_f:
    reader = DictReader(in_f)
    for line in reader:
        data['day'].append(line['time_received_isoformat'].day)
        data['time'].append(line['time_received_isoformat'].hour * 60 + line['time_received_isoformat'].minute)
        data = DataFrame(data)
        plot = seaborn.stripplot(data=data, x='day', y='time')
        plot.get_figure().savefig('/home/jacob/Projects/CIS2302/CW2/ddd_cw2/temporal_graphs/' + 'days_stripplot' + '.png')
        pyplot.close()