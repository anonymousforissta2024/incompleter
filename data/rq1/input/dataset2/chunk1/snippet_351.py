#Source: https://stackoverflow.com/questions/58575057/update-throwing-typeerror-serializer-update-got-an-unexpected-keyword-argum
urlpatterns = [
    path('sendsms/', SMSView.as_view(), name="send_sms"),
    path('viewsms/', SMSView.as_view(), name="view_sms"),
]