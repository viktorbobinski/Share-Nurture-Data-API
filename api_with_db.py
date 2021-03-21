from flask import Flask
from flask_restful import Api, Resource, reqparse, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)


class VideoModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    likes = db.Column(db.Integer, nullable=False)
    views = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Video(name={name}, likes={likes}, views={views}"


video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type=str, help="Name of the video is required", required=True)
video_put_args.add_argument("likes", type=int, help="Likes on the video are required", required=True)
video_put_args.add_argument("views", type=int, help="Views on the video are required", required=True)

resource_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'likes': fields.Integer,
    'views': fields.String
}

db.drop_all()
db.create_all()


class Videos(Resource):
    @marshal_with(resource_fields)
    def get(self):
        videos = VideoModel.query.all()
        return videos


class Video(Resource):
    @marshal_with(resource_fields)
    def get(self, video_id):
        video = VideoModel.query.get(video_id)
        return video, 200

    @marshal_with(resource_fields)
    def put(self, video_id):
        args = video_put_args.parse_args()
        video = VideoModel(id=video_id, name=args['name'], likes=args['likes'], views=args['views'])
        db.session.add(video)
        db.session.commit()
        return video, 201

    def delete(self, video_id):
        VideoModel.query.filter_by(id=video_id).delete()
        db.session.commit()
        return "", 204


api.add_resource(Video, "/videos/<int:video_id>")
api.add_resource(Videos, "/videos")


if __name__ == "__main__":
    app.run(debug=True)

