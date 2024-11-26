@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if not username or not password:
            return render_template("login.html", error="Please enter both username and password.")

        user = get_user(username)
        if user and user.check_password(password):
            login_user(user)
            return redirect(url_for("index"))
        else:
            return render_template("login.html", error="Invalid username or password.")
    
    return render_template("login.html")
