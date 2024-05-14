#Source: https://stackoverflow.com/questions/64985316/django-adding-data-into-model-from-nested-json-returning-typeerror-nonetype-o
for i in card_data:
  Card.objects.update_or_create(
    id=i.get('id'),

    defaults={
      'name':       i.get('name'),
      'card_faces': i.get('card_faces'),
      'f_name':     i.get('card_faces')[0].get('name'),
      'b_name':     i.get('card_faces')[1].get('name'),
    }
  )