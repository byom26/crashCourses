from flask import Flask, request
from flask_restful import Api, Resource, abort, reqparse, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)


class VideoModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    views = db.Column(db.Integer, nullable=False)
    likes = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Video(name={name}, views={views}, likes={likes})"

# db.create_all() #=> Run it only for the first time

video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type=str, help="Invalid name of the video", required=True)
video_put_args.add_argument("views", type=str, help="Invalid views on the video", required=True)
video_put_args.add_argument("likes", type=str, help="Invalid likes on the video", required=True)

video_patch_args = reqparse.RequestParser()
video_patch_args.add_argument("name", type=str, help="Invalid name of the video")
video_patch_args.add_argument("views", type=str, help="Invalid views on the video")
video_patch_args.add_argument("likes", type=str, help="Invalid likes on the video")

resource_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'views': fields.Integer,
    'likes': fields.Integer
}

# videos = {}

# def abort_ifNot_exists(video_id):
#     if video_id not in videos:
#         abort(404, message="Video ID doesn't exists!")

# def abort_if_exists(video_id):
#     if video_id in videos:
#         abort(409, message="Video already exists with that id!")


class Video(Resource):
    @marshal_with(resource_fields)
    def get(self, video_id):
        result = VideoModel.query.filter_by(id=video_id).first()
        if not result:
            abort(404, message="Video with that given id doesn't exists!")
        return result
        # abort_ifNot_exists(video_id)
        # return videos[video_id]

    @marshal_with(resource_fields)
    def put(self, video_id):
        # - Using database
        args = video_put_args.parse_args()
        result = VideoModel.query.filter_by(id=video_id).first()
        if result:
            abort(409, message="Video with that given id already exists!")
        video =VideoModel(id=video_id, name=args['name'], views=args['views'], likes=args['likes'])
        db.session.add(video)
        db.session.commit()
        return video, 201

        #  - Not feasible way of getting the data - 
        # print(request.form)
        # print(request.form['likes'])
        
        # - Using data in the form of dictionaries
        # abort_if_exists(video_id)
        # args = video_put_args.parse_args()
        # videos[video_id] = args
        # return {video_id: args}
        # return videos[video_id], 201

    @marshal_with(resource_fields)
    def patch(self, video_id):
        args = video_patch_args.parse_args()
        result = VideoModel.query.filter_by(id=video_id).first()
        if not result:
            abort(404, message="Video doesn't exists, can't update!")
        if args['name']: # By default it will contain None, So if any new values we are passing then it will update it.
            result.name = args['name']
        if args['views']:
            result.views = args['views']
        if args['likes']:
            result.likes = args['likes']
        # db.session.add(result) => While updating we don't need to add it to the db as it already exists.
        db.session.commit()
        return result

    def delete(self, video_id):
        abort_ifNot_exists(video_id)
        del videos[video_id]
        return "Video Deleted!", 204


api.add_resource(Video, "/video/<int:video_id>")


# names = {
#     "byom": {"age": 24, "gender": "male"},
#     "test": {"age": 30, "gender": "female"}
# }

# class HelloWorld(Resource):
#     def get(self, name):
#         return names[name]
#         return {'data': 'Get Request!'}
#         return {
#             'name': name,
#             'age': age
#         }

#     def post(self):
#         return {'data': 'Post Request!'}

# api.add_resource(HelloWorld, "/hello")
# api.add_resource(HelloWorld, "/hello/<string:name>/<int:age>")
# api.add_resource(HelloWorld, "/hello/<string:name>")

if __name__ == "__main__":
    app.run(debug=True)