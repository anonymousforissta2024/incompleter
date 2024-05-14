#Source: https://stackoverflow.com/questions/67133185/sqlite3-flask-discord-bot-dashboard-typeerror-nonetype-object-is-not-subscrip
@app.route("/serveurs/<int:serveur_id>")
def serveur(serveur_id):
    if 'token' not in session:
        return redirect("https://discord.com/api/oauth2/authorize?client_id=787982190776287282&redirect_uri=https%3A%2F%2FMEE0-1.devteaming.repl.co%2Foauth%2Fdiscord&response_type=code&scope=identify%20guilds")
    serveur_info = get_serveur_info(serveur_id)
    if not serveur_info:
        return redirect('/dashboard')
        
    with sqlite3.connect("dashboard.sqlite3") as db:
        cursor = db.cursor()
        cursor.execute(f"SELECT * FROM dashboardconfig WHERE guilds_id = {serveur_info['id']}")
        data = cursor.fetchone()
    print(data)
    mod = bool(data[2])
    music = bool(data[2])
    fun = bool(data[2])
    return render_template("serveur.html", serveur=serveur_info, mod=mod, music=music, fun=fun)