#Source: https://stackoverflow.com/questions/55113041/attributeerror-module-flask-app-has-no-attribute-route
from flask import Flask, render_template, redirect, url_for, request, session, flash, app, Blueprint, jsonify

@app.route('/autocomplete',methods=['GET'])
def autocomplete():
    database='backbone_test'
    db=client[database]
    all_names=list(db.ids.find({},{"current_name":1,"_id":0}))
    return json.dumps(all_names) 