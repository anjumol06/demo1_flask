# this is pyton configuration file


from flask import Flask ,render_template#this is a flask package

app=Flask(__name__)

@app.route('/')# default api view function
def home():
    return render_template('home.html')


@app.route('/s2s/api/signup')
def user_signup():
    return "this is a user signup page"\

@app.route('/anju/api/login')
def user_login():
    return "this is a user login page"

@app.route('/anju/api/about')
def user_about():
    return "this is about our webpage "





if __name__=="__main__":
    app.run(debug=True)