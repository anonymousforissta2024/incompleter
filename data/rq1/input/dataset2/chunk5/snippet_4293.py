#Source: https://stackoverflow.com/questions/59984422/typeerror-datetime-datetime-object-is-not-callable-when-i-generate-lazydateti
paid_at = lazy(datetime.date.today, datetime.date)