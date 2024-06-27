import flask

app = flask.Flask(__name__)

@app.route('/')
def index():
    return flask.render_template('index.html') 

#-----------------
# Do NOT Write Code Above This Line
#-----------------

@app.route('/done')
def form_submit():
    first_name = flask.request.args['fname']
    last_name = flask.request.args['lname']
    city = flask.request.args['city']
    state = flask.request.args['state']
    age = flask.request.args['age']
    bio = flask.request.args['bio']
    website = flask.request.args['website']
    return flask.render_template('profile.html', fname=first_name, lname=last_name, city=city, state=state, age=age, bio=bio, website=website)

#-----------------
# Do NOT Write Code Below This Line
#-----------------

app.run(host='0.0.0.0', port='5000')

