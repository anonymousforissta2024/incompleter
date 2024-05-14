#Source: https://stackoverflow.com/questions/58030538/typeerror-str-object-is-not-callable-on-request-to-api
app_name = 'ads'
urlpatterns = [
    # ex: /ads/
    url(r'^$', views.ListBrand.as_view(), name='brand_list'),
]