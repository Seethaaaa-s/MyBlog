from flask import Flask, redirect,render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
from models import db,post
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False


db.init_app(app)

@app.route('/')
def home():
    posts=post.query.all()
    return render_template('home.html',posts=posts)
@app.route('/post/add',methods=['GET','POST'])
def add_post():
    if request.method=='POST':
        title=request.form['title']
        author=request.form['author']
        content=request.form['content']
        post1=post(title=title,content=content,author=author)
        db.session.add(post1)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('add_post.html')
@app.route('/post/edit/<int:id>',methods=['GET','POST'])
def edit_post(id):
    Post=post.query.get(id)
    if request.method=='POST':
        Post.title=request.form['title']
        Post.author=request.form['author']
        Post.content=request.form['content']
        db.session.commit()
        return redirect(url_for('post_details',id=Post.id))
    return render_template ('edit_post.html',post=Post)

@app.route('/post/<int:id>')
def post_details(id):
    Post=post.query.get(id)
    return render_template('post_details.html',post=Post)
@app.route('/post/delete/<int:id>')
def delete_post(id):
    Post=post.query.get(id)
    db.session.delete(Post)
    db.session.commit()
    return redirect(url_for('home'))
@app.route('/About')
def about():
    return render_template('about.html')
if __name__=='__main__':
    app.run(debug=True)
