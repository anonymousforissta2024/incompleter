#Source: https://stackoverflow.com/questions/41529292/tornado-rediret-incur-typeerror-initialize-missing-1-required-positional-argu
import bcrypt
import concurrent.futures
#import MySQLdb
#import markdown
import os.path
import re
import subprocess
#import torndb
import tornado.escape
from tornado import gen
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import unicodedata
from tornado.options import define, options

define("port",default=8889,help='run on the given port',type=int)


class HomeHandler(tornado.web.RequestHandler):

    def get(self):
        #login here
        self.render('index.html')

    def post(self):
        def readcodebook(codebook):
            with open(codebook,'r+') as f:
                CodeLines=f.read().split('\n')
                combinations={}
                for c in CodeLines:
                    if len(c)>0:
                        combinations[c.split('\t')[0]]=c.split('\t')[1]
            return combinations
        UserFile='/home/john/PyServer/Users/codebook.txt'
        CodeBook=readcodebook(UserFile)

        if self.get_argument("login") in CodeBook.keys():
            if CodeBook[self.get_argument("login")]==self.get_argument("password"):
                #correct pwd
                self.redirect(self.get_argument("next","/display/"))
            else:
                #incorrect pwd
                self.render("index.html", error='incorrect password!')
                return
        else:
            #user not found
            self.render("index.html", error="account not found!")
            return


class DisplayHandler(tornado.web.RedirectHandler):
    def get(self):
        self.render("displaycontent.html")
    pass


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", HomeHandler),
            (r"/display/", DisplayHandler),
        ]
        settings = dict(
            #blog_title=u"Tornado Blog",
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__), "static"),
            #ui_modules={"Entry": EntryModule},
            #xsrf_cookies=True,
            #cookie_secret="__TODO:_GENERATE_YOUR_OWN_RANDOM_VALUE_HERE__",
            #login_url="/auth/login",
            debug=True,
        )
        tornado.web.Application.__init__(self,handlers,**settings)

if __name__=="__main__":
    tornado.options.parse_command_line()
    http_server=tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()