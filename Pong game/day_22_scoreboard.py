from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 50, "normal")


class Scoreboard(Turtle):
    
    def __init__(self, position):
        super().__init__()
        self.score_r = 0
        self.score_l = 0
        self.hideturtle()
        self.penup()
        self.goto(position)
        self.color("white")
        self.update_scoreboard()
        
        
    def update_scoreboard(self):
        self.write(f"{self.score_l}  {self.score_r}", align= ALIGNMENT, font= FONT) 
        
        
        
    def increase_right_score(self):
        self.score_r += 1
        self.clear()
        self.update_scoreboard()
        
    def increase_left_score(self):
        self.score_l += 1
        self.clear()
        self.update_scoreboard()
        
    
                    

























