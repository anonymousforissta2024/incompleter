#Source: https://stackoverflow.com/questions/58860465/typeerror-object-of-type-decimal-is-not-json-serializable-during-django-data-mi
data = {
        'premium': obj.amount * obj.persons,
    }
proposal.new_column = data
proposal.save()