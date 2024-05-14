#Source: https://stackoverflow.com/questions/50037254/pathaccounts-includeaccounts-urls-nameerror-name-accounts-is-not-def
urlpatterns = [
    path('signup', views.signup, name="signup"),
    path('login', views.login, name="login"),
    path('logout', views.logout, name="logout"),
]