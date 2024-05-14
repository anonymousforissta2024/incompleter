#Source: https://stackoverflow.com/questions/46237181/type-error-when-using-date-from-a-django-form-i-get-combine-argument-1-must
dato = form.cleaned_data['dato']
dato = datetime.datetime.strptime(dato, "%Y-%m-%d")