#!/usr/bin/env python3

from app import app
from config import db
from models import Game, Player, Level

if __name__ == '__main__':
    with app.app_context():
        
        print("Clearing db...")
        Game.query.delete()
        Level.query.delete()
        Player.query.delete()

        db.session.commit()
        
        print("Seeding...")
        print("Seeding levels...")

        level1 = Level(name="1-a", difficulty="Beginner", text="Hello, World!")
        level2 = Level(name="1-b", difficulty="Beginner", text="Practice makes perfect.")
        level3 = Level(name="1-c", difficulty="Beginner", text="Keyboard ninja in training.")
        level4 = Level(name="1-d", difficulty="Beginner", text="The quick brown fox jumps over the lazy dog.")
        level5 = Level(name="1-e", difficulty="Beginner", text="Keyboard ninja in training.")
        level6 = Level(name="1-f", difficulty="Beginner", text="Coding is fun!")
        level7 = Level(name="1-g", difficulty="Beginner", text="Type your way to victory.")
        level8 = Level(name="1-h", difficulty="Beginner", text="Challenge accepted, fingers ready!")
        level9 = Level(name="1-i", difficulty="Beginner", text="Words are your playground.")
        level10 = Level(name="1-j", difficulty="Beginner", text="Unlock the keyboard wizard in you.")
        level11 = Level(name="2-a", difficulty="Intermediate", text="The quick brown fox jumps over the lazy dog.")
        level12 = Level(name="2-b", difficulty="Intermediate", text="A journey of a thousand miles begins with a single step.")
        level13 = Level(name="2-c", difficulty="Intermediate", text="In the midst of winter, I found there was, within me, an invincible summer.")
        level14 = Level(name="2-d", difficulty="Intermediate", text="Success is not final, failure is not fatal: It is the courage to continue that counts.")
        level15 = Level(name="2-e", difficulty="Intermediate", text="The only limit to our realization of tomorrow will be our doubts of today.")
        level16 = Level(name="2-f", difficulty="Intermediate", text="Life is what happens when you're busy making other plans.")
        level17 = Level(name="2-g", difficulty="Intermediate", text="Believe you can and you're halfway there.")
        level18 = Level(name="2-h", difficulty="Intermediate", text="The greatest glory in living lies not in never falling, but in rising every time we fall.")
        level19 = Level(name="2-i", difficulty="Intermediate", text="It does not matter how slowly you go, as long as you do not stop.")
        level20 = Level(name="2-j", difficulty="Intermediate", text="The best way to predict the future is to create it.")
        level21 = Level(name="3-a", difficulty="Advanced", text="The entropy of the universe tends to a maximum, but human creativity strives to defy that cosmic inevitability.")
        level22 = Level(name="3-b", difficulty="Advanced", text="Quantum mechanics introduces us to a world where particles exist in multiple states until observed, challenging our classical intuitions.")
        level23 = Level(name="3-c", difficulty="Advanced", text="In the realm of artificial intelligence, neural networks emulate the complexity of the human brain, pushing the boundaries of machine learning.")
        level24 = Level(name="3-d", difficulty="Advanced", text="Chaos theory reveals the underlying order in seemingly random systems, demonstrating the exquisite sensitivity to initial conditions.")
        level25 = Level(name="3-e", difficulty="Advanced", text="Einstein's theory of relativity revolutionized our understanding of space and time, showing the interplay between mass, energy, and gravity.")
        level26 = Level(name="3-f", difficulty="Advanced", text="The intricacies of genetic code govern the blueprint of life, unraveling the mysteries of inheritance and evolution.")
        level27 = Level(name="3-g", difficulty="Advanced", text="Nanotechnology manipulates matter at the molecular and atomic levels, opening doors to innovations with profound implications.")
        level28 = Level(name="3-h", difficulty="Advanced", text="Dark matter and dark energy, constituting the majority of the cosmos, challenge physicists to decipher the enigma of the universe's composition.")
        level29 = Level(name="3-i", difficulty="Advanced", text="The intersection of philosophy and quantum physics beckons us to ponder the nature of reality and the role of consciousness in shaping it.")
        level30 = Level(name="3-j", difficulty="Advanced", text="Cryptocurrencies employ blockchain technology, disrupting traditional finance and ushering in a decentralized era of digital transactions.")

        levels = [ level1, level2, level3, level4, level5, level6, level7, level8, level9, level10, level11, level12, level13, level14, level15, level16, level17, level18, level19, level20, level21, level22, level23, level24, level25, level26, level27, level28, level29,
        level30 ]

        db.session.add_all(levels)
        db.session.commit()

        print("Seeded all levels.")
        print("Done seeding.")