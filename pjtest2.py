from  flask_script import Manager
from  flask import  Flask, render_template
from  flask_moment import  Moment
from  flask_bootstrap import Bootstrap
from  datetime import  datetime
from  flask_wtf import Form
from  wtforms import StringField,SubmitField
from  wtforms.validators import Required
app=Flask(__name__)
app.config['SECRET_KEY']='hard to guess string'
bootstrap=Bootstrap(app)
moment=Moment(app)
@app.route('/')
def index():
   return render_template('index.html',current_time=datetime.utcnow())
@app.route('/user/<name>')
def user(name):
    return render_template('user.html',name=name)
class NameForm(Form):
    name=StringField('What is your name?',validators=[Required()])
    submit=SubmitField('Submit')




if __name__ == '__main__':
    app.run(debug=True)