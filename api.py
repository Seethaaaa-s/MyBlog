from flask_restful import Resource,Api
from models import db,post
from flask import jsonify, request,make_response
api=Api()
class Postresource(Resource):
    def get(self,id=None):
        if id is None:
            posts=post.query.all()
            list=[]
            for Post in posts:
                list.append({
                    'id':Post.id,
                    'title':Post.title,
                    'content':Post.content,
                    'author':Post.author
                })
            return list,200
        else:
            Post=post.query.get(id)
            return {'id':Post.id,'title':Post.title,'content':Post.content,'author':Post.author}



    def post(self):
        data=request.get_json()
        Post=post(tile=data['title'],content=data['content'],author=data['author'])
        db.session.add(Post)
        db.session.commit()

        return make_response(jsonify({'message':"Post Added Succesfully",'id':Post.id}),201)
    def put(self,id):
        Post=post.query.get(id)
        data=request.get_json()
        Post.title=data['title']
        Post.content=data['content']
        Post.author=data['author']
        db.session.commit()
        return jsonify({'message':'post updated susccesfully'})
    def delete(self,id):
        Post=post.query.get(id)
        db.session.delete(Post)
        db.session.commit()
        return make_response(jsonify({'messsage':'Post Delted Succesfully'}),200)
api.add_resource(Postresource,'/api/posts','/api/posts/<int:id>')