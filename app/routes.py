from flask import render_template, request, jsonify, session, redirect, url_for
from app import app
from app import db

from app.models.UserModel import User
from app.models.PostModel import Post
from app.models.LikePostModel import LikePost

from app.models.Schemas import UserSchema, PostSchema, LikePostSchema

@app.route("/login", methods=['GET','POST'])
def login():
  if(request.method == 'POST'):
    form = request.json["form_data"]

    # db.session.add(UserSchema().load({"username":"@maria","name":"Maria da silva","description":"toppppp","password":"123"}))
    # db.session.commit()
    user = User.query.filter(User.username == form["user"], User.password == form["passw"]).first()
    if(user):
      session["user"]=user.id
      url = "/"
      return jsonify({'status':'1','url':url})
      
    else:
      return jsonify({'status':'2'})

  return render_template("login.html")  

@app.route("/logout")
def logout():
    del(session["user"])
    return redirect(url_for('login'))

@app.route("/")
def index():
    try:
        dataUser = User.query.filter_by(id = session["user"]).first()
        dataUser = UserSchema(exclude=["password"]).dump(dataUser)

        posts = Post.query.options(db.joinedload(Post.user)).order_by(Post.id.desc()).all()
        posts = PostSchema(many=True).dump(posts)

        result = LikePost.query.with_entities(LikePost.liked_post).filter_by(liked_by=session['user']).all()
        postsLiked = ()
        for i in result:
            postsLiked += i

        return render_template("index.html", posts=posts, dataUser=dataUser, postsLiked=postsLiked)

    except Exception as e:
        print(e)
        return redirect(url_for('login'))

@app.route("/insere_post", methods=['POST'])
def insere_post():
    form = request.json["form_data"]
    post = PostSchema().load({"created_by":form['createdBy'],"title":form['title'],"text":form['text']})
    db.session.add(post)
    db.session.commit()
    post = PostSchema().dump(post)
    print(post)

    return jsonify({'status':'1','post':post})

@app.route("/like_post", methods=['POST'])
def like_post():
    try:
        form = request.json["form_data"]
        print(form)

        result = LikePost.query.filter(LikePost.liked_by == form["liked_by"], LikePost.liked_post == form["liked_post"]).first()
        print(result)
        post = Post.query.filter_by(id = form["liked_post"]).first()
        
        if(result):
            db.session.delete(result)
            db.session.commit()
            action = "dislike"
            post.num_likes -= 1
        else:
            like = LikePostSchema().load(form)
            db.session.add(like)
            db.session.commit()
            action = "like"
            post.num_likes += 1

        db.session.add(post)
        db.session.commit()
        
        return jsonify({'status':'1','action':action})

    except Exception as e:
        return jsonify({'status':'2','error':e})

@app.route("/delete_post/<int:idPost>", methods=['DELETE'])
def delete_post(idPost):
    post = Post.query.filter(Post.id == idPost).first()
    db.session.delete(post)
    db.session.commit()

    return jsonify({'status':'1'})

@app.route("/comment_post/<int:idPost>", methods=["POST"])
def comment_post(idPost):
    form = request.json["form_data"]
    form['of'] = idPost
    db.session.add(form)
    db.session.commit()

    return jsonify({'status':'1', 'comment':form})
