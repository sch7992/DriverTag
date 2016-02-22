__author__ = 'SWEN356 Team 4'

from app import app
from flask_oauth import OAuth
from flask import render_template, redirect, url_for, session, request

oauth = OAuth()
facebook = oauth.remote_app('facebook',
    base_url='https://localhost:5000',
    request_token_url=None,
    access_token_url='/oauth/access_token',
    authorize_url='https://www.facebook.com/dialog/oauth',
    consumer_key='966689803422128',
    consumer_secret='5ebcacfed9b216675ed00ff074d87c4b',
    request_token_params={'scope':'email'},
)


@facebook.tokengetter
def get_fb_token(token=None):
    return session.get('facebook_token')


@app.route('/oauth-authorized')
@facebook.authorized_handler
def oauth_authorized(resp):
    next_url = facebook.request.args.get('next') or url_for('index', _external=True)
    if resp is None:
        facebook.flash('Your sign in request was denied.')
        return redirect(next_url)

    session['facebook_token'] = (resp['oauth_token'], resp['oauth_token_secret'])
    session['facebook_user'] = resp['email']
    facebook.flash('You were signed in as %s' % resp['email'])
    return redirect(next_url)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/login')
def login():
    return facebook.authorize(callback=url_for('index', _external=True))



