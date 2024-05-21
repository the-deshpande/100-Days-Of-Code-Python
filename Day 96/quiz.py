from random import shuffle


class House:
    def __init__(self, character: dict):
        self.question = f"What house was {character.get('name')} form?"
        self.options = ['Gryffindor', 'Slytherin', 'Hufflepuff', 'Ravenclaw']
        self.correct_answer = character.get('house')


class Spells:
    def __init__(self, spells: list):
        self.question = f"What does the spell {spells[0].get('name')} do?"
        self.options = [spells[0].get('description'), spells[1].get('description'),
                        spells[2].get('description'), spells[3].get('description')]
        shuffle(self.options)
        self.correct_answer = spells[0].get('description')
