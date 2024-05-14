#Source: https://stackoverflow.com/questions/64081130/flask-typeerror-object-of-type-cycle-is-not-json-serializable
@app.route("/test", methods=["GET", "POST"])
@login_required
def test():

  if request.is_xhr:

    try:

      json_response = {
        "result": "success"
      }

    except Exception as e:
      err = _except(line=sys.exc_info()[-1].tb_lineno, error=e, function_name=what_func(), script_name=__file__)
      json_response = {"result": "failure", "msg": err}

    return jsonify(json_response)

  else:
    return redirect("/not-found")

  return ''