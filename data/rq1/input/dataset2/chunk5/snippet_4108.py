#Source: https://stackoverflow.com/questions/52626178/sessions-in-web-py-causing-nameerror
app = web.application(urls, globals())
# Session
session = web.session.Session(app, web.session.DiskStore("sessions"), initializer={'user': 'none'})
session_data = session._initializer

render = web.template.render("Views/Templates", base="MainLayout", globals={'session': session_data, 'current_user': session_data['user']})