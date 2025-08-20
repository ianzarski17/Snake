from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Courier', 24, 'normal')

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.ht()
        self.score = 0
        with open('data.txt') as file:
            self.highscore = int(file.read())
        self.color('white')
        self.teleport(0, 260)
        self.update()

    def update(self):
        self.clear()
        self.write(f"Score: {self.score}    Highscore: {self.highscore}", align= ALIGNMENT,font= FONT)


    def score_up(self):
        self.score += 1
        self.update()

    def refresh(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open('data.txt', mode='w') as data:
                data.write(f"{self.highscore}")
        self.score = 0
        self.update()



