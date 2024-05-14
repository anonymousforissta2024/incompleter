#Source: https://stackoverflow.com/questions/55113041/attributeerror-module-flask-app-has-no-attribute-route
from flask import Flask, render_template, Blueprint, jsonify, session
import jinja2

class MyApp(Flask):
  def __init__(self):
    Flask.__init__(self, __name__)
    self.jinja_loader = jinja2.ChoiceLoader([self.jinja_loader,jinja2.PrefixLoader({}, delimiter = ".")])
    def create_global_jinja_loader(self):
        return self.jinja_loader

    def register_blueprint(self, bp):
        Flask.register_blueprint(self, bp)
        self.jinja_loader.loaders[1].mapping[bp.name] = bp.jinja_loader

app = MyApp()

from xyzapp.autocomplete import autocomplete
from xyzapp.blueprint_folder_1.some_file import bp_1

app.register_blueprint(bp_1)