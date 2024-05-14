#Source: https://stackoverflow.com/questions/52154852/typeerror-loadshortlink-got-multiple-values-for-argument-shortlink
path('s/<str:shortlink>',views.loadshortlink, name="get_longlink")