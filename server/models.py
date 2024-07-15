from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates
from config import db

# Write models below: Game, Level, Player

# ===== Game =====
class Game(db.Model, SerializerMixin):
    __tablename__ = 'games'

    # Properties
    id = db.Column(db.Integer, primary_key=True)
    player_id = db.Column(db.Integer, db.ForeignKey('players.id'))
    level_id = db.Column(db.Integer, db.ForeignKey('levels.id'))
    input = db.Column(db.String, nullable=False)
    time = db.Column(db.String, nullable=False)
    accuracy = db.Column(db.Float, nullable=False)

    # Relationships
    player = db.relationship('Player', back_populates='games')
    level = db.relationship('Level', back_populates='games')

    # Serialization
    serialize_rules = ['-player.games', '-level.games']

    # Validations

    def __repr__(self) -> str:
        return f"<Game id: {self.id} | Player id: {self.player_id} | Level id: {self.level_id}>"

# ===== Level =====
class Level(db.Model, SerializerMixin):
    __tablename__ = 'levels'

    # Properties
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    difficulty = db.Column(db.String)
    text = db.Column(db.String)

    # Relationships
    games = db.relationship('Game', back_populates='level')

    # Serialization
    serialize_rules = ['-games']
    # Validations

    def __repr__(self) -> str:
        return f"<Level id: {self.id} | {self.name} | {self.difficulty}>"

# ===== Player =====
class Player(db.Model, SerializerMixin):
    __tablename__ = 'players'

    # Properties
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    # Relationships
    games = db.relationship('Game', back_populates='player', cascade='all, delete-orphan')

    # Serialization
    serialize_rules = ['-games']

    # Validations
    @validates('name')
    def validate_name(self, key, name):
        if isinstance(name, str) and len(name) >= 3:
            self.name = name
        else:
            raise ValueError("Name must be a string with more than 3 characters.")

    def __repr__(self) -> str:
        return f"<Player id: {self.id} | Name: {self.name}>"