from datetime import datetime
from flask import flash, redirect, render_template

# local packages
from app import app
from .forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    time = { 'now' : str(datetime.now())}
    return render_template('index.html', time = time)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="%s", remember_me=%s' %
              (form.openid.data, str(form.remember_me.data)))
        return redirect('/index')
    return render_template('login.html',
                           title='Sign In',
                           form=form)
