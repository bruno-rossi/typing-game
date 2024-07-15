#!/usr/bin/env python3

from flask import request, session, make_response
from config import app, db
import os
from models import Game, Level, Player

@app.route('/levels/', methods=['GET', 'POST'])
# Write levels functions here!
def levels():

    if request.method == 'GET':
        levels = [level.to_dict() for level in Level.query.all()]

        return levels, 200

    if request.method == 'POST':

        try:
            new_level = Level(
                name=request.get_json()['name'],
                difficulty=request.get_json()['difficulty'],
                text=request.get_json()['text']
            )

            db.session.add(new_level)
            db.session.commit()

            return new_level.to_dict(), 201
        
        except Exception as e:
            return {'error': str(e)}, 400

@app.route('/games/', methods=['GET', 'POST'])
# Write games functions here!
def games():

    if request.method == 'GET':
        games = [game.to_dict() for game in Game.query.all()]

        return games, 200

    if request.method == 'POST':

        try:
            new_game = Game(
                player_id=request.get_json()['player_id'],
                level_id=request.get_json()['level_id'],
                input=request.get_json()['input'],
                time=request.get_json()['time'],
                accuracy=request.get_json()['accuracy']
            )

            db.session.add(new_game)
            db.session.commit()

            return new_game.to_dict(), 201
        
        except Exception as e:
            return {'error': str(e)}, 400

@app.route('/players/', methods=['GET', 'POST'])
def all_players():

    if request.method == 'GET':
        players = [player.to_dict() for player in Player.query.all()]

        return players, 200
    
    if request.method == 'POST':

        try:
            new_player = Player(
                name=request.get_json()['name']
            )

            db.session.add(new_player)
            db.session.commit()

            return new_player.to_dict(), 201
        
        except Exception as e:
            return {"error": str(e)}, 400

@app.route('/players/<int:id>/', methods=['GET', 'PATCH', 'DELETE'])
# Write player patch and delete functions here!
def player_by_id(id):

    player = Player.query.filter(Player.id == id).first()

    if player:
        if request.method == 'GET':
            try:
                return player.to_dict(), 200
            
            except Exception as e:
                return {"error": str(e)}, 400
            
        if request.method == 'PATCH':
            for attr in request.get_json():
                setattr(player, attr, request.get_json()[attr])

            db.session.add(player)
            db.session.commit()

            return player.to_dict(), 202
        
        if request.method == 'DELETE':
            db.session.delete(player)
            db.session.commit

            return {}, 204

    else:
        return { "error": "Player not found" }, 404