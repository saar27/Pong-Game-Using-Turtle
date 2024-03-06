from turtle import Screen
from day_22_paddle import Paddle
from day_22_ball import Ball
from day_22_scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height= 600)
screen.bgcolor("black")
screen.title("Pong game")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard((0, 230))

 
   
screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")


game_in_on = True
while game_in_on:
    screen.update()
    ball.move()
    time.sleep(ball.move_speed) 
    
    
    #detect collidion with wall.
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
        
    
    #detect collidion with paddel.
    if (ball.xcor() > 320 and ball.distance(r_paddle) < 50) or (ball.xcor() < -320 and ball.distance(l_paddle) < 50):
        ball.bounce_x()
        
        
    
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.increase_left_score()
    elif ball.xcor() < -380:
        ball.reset_position()
        scoreboard.increase_right_score()
                 
        
        
            
               
















screen.exitonclick()