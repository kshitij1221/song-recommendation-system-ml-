@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        if not username or not email or not password:
            return render_template("signup.html", error="Please enter all fields.")

        user = get_user(username)
        if user:
            return render_template("signup.html", error="Username already exists.")

        save_user(username, email, password)
        user = get_user(username)
        login_user(user)
        return redirect(url_for("index"))

    return render_template("signup.html")