#Source: https://stackoverflow.com/questions/49222033/raise-typeerrorrepro-is-not-json-serializable
from marshmallow import Schema, fields

class Product():
  def __init__(self, ident, name, description, category):
      self.ident = ident
      self.name = name
      self.description = description
      self.category = category

  def __repr__(self):
      return '<Expense(name={self.description!r})>'.format(self=self)

class ProductSchema(Schema):
      ident = fields.Str()
      name = fields.Str()
      category = fields.Str()
      description = fields.Str()