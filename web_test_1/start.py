from flask import Flask,render_template,redirect,request
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)


all_posts = [{'name': 'vishnu','age': 18,'department': 'mct'},{'name': 'vishal','age': 17,'department': 'mct'},{'name': 'victor','age': 18,'department': 'mct'}]

#app.config[' SQLALCHEMY_DATABASE_URI '] = 'sqlite:///posts1.db'
#db = SQLAlchemy(app)

#class Blogpost(db.Model):
#	id = db.Column(db.Integer,primary_key = True)
#	name = db.Column(db.String(100), nullable = False)
#	content = db.Column(db.Text,nullable = True)
#	author = db.Column(db.String(50) , nullable = False,default = 'N/A')
	
#	def __repr__(self):
#		return 'Blogpost' + str(self.id)
	
@app.route('/')
def hello():
    return render_template('base.html')
    
@app.route('/home')
def home():
	return render_template("home.html") 
	   
@app.route('/posts' , methods = ['GET','POST'])
def posts():
#	if request.method == 'POST':
#		post_name = request.form['title']
#		post_content = request.form['content']
#		new_post = Blogpost(name = post_name,content = post_content,author = "vishnu")
#		
#		db.session.add(new_post)
#		db.session.commit()
#		return redirect('/posts')
#	else:
#		all_posts = Blogpost.query.all()
	
		return render_template("posts.html", content = all_posts)	

if __name__ == "__main__":
	app.run(debug= True)  
