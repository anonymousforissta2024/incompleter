#Source: https://stackoverflow.com/questions/60123122/typeerror-get-got-an-unexpected-keyword-argument-project-id-in-flask-applica
from flask import request
from flask_restful import Resource
from  Model import db, Project, ProjectSchema

projects_schema = ProjectSchema(many=True)
project_schema = ProjectSchema()

"""
Get project by id
"""
def get_by_id(project_id):
    project = Project.query.filter_by(id=project_id).first()
    project = projects_schema.dump(project).data
    return {'status': 'success', 'data': project}, 200