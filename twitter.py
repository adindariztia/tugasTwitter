import json
from flask import Flask, jsonify, Blueprint, request
from flask_restful import Resource, Api, reqparse, inputs, abort

user = [{
    "username": "John",
    "email": "john@haha.com",
    "password": "Hoooa123",
    "fullname": "John rukmana"
},
{
    "username": "jeff",
    "email": "jeff@haha.com",
    "password": "Hahaha123",
    "fullname": "John rukmana"
}]

tweet = [{
    "email": "john@haha.com",
    "tweet": "Ini ceritanya tweet Twitter yah"
},
{
    "email": "jeff@haha.com",
    "tweet": "Ini ceritanya tweet Twitter yah"
}]

class signUp(Resource):
    def post(self):
        user.append(request.json)
        with open('data.txt', 'w') as outfile:
            json.dump(user, outfile)
        return user[-1], 201


class showAllUser(Resource):
    def get(self):
        with open('data.txt') as filejson:
            dataUser = json.load(filejson)
        return dataUser
        # return user

class showAllTweet(Resource):
    def get(self):
        with open('tweet.txt') as json_file:
            dataTweet = json.load(json_file)
            
        return dataTweet

class login(Resource):
    def post(self):
        # email = request.json[]
        with open('data.txt') as json_file:
            for user in json.load(json_file):
                # print(user['email'])
                
        #     # print(data['email'], request.json["email"], data['email'] == request.json["email"])
        #     # print(data['password'], request.json["password"], data['password'] == request.json["password"])

                if (user['email'] == request.json["email"]):
                    if (user['password'] == request.json["password"]):
                        return "Login successful!"
                    else:
                        return "email/password salah" 
            
            return "user does not exist"

class postTweet(Resource):
    def post(self):
        with open('data.txt') as json_file:
            dataUser = json.load(json_file)
            for data in dataUser:
                if (data['email'] == request.json['email']):
                    tweet.append(request.json)
                    with open('tweet.txt', 'w') as outfile:
                        json.dump(tweet, outfile)
        #         return tweet[-1],201

              
        # return "email tidak terdaftar"
        

class bacaTweet(Resource):
    def get(self):
        with open('tweet.txt') as json_file:
            dataTweet = json.load(json_file)
            return dataTweet

class deleteTweet(Resource):
    def delete(self):
        with open('tweet.txt') as json_file:
            dataTweet = json.load(json_file)
            for tweet in dataTweet:
                if (tweet['email'] == request.json['email']):
                    print('masuk1')
                    if tweet['tweet'] == request.json['tweet']:
                        print('masuk2')
                        dataTweet.remove(tweet)
                        return tweet
                    else:
                        return "tweet doesnt exist"
            
            return "email doesnt exist"

twitter_api = Blueprint('curltwitter/twitter', __name__)
api = Api(twitter_api)

api.add_resource(signUp, '/api/twitter/signup')
api.add_resource(showAllUser, '/api/twitter/showuser')
api.add_resource(showAllTweet, '/api/twitter/showtweet')
api.add_resource(login, '/api/twitter/login')
api.add_resource(postTweet,'/api/twitter/ngetwit')
api.add_resource(bacaTweet, '/api/twitter/bacatweet')
api.add_resource(deleteTweet, '/api/twitter/delete')