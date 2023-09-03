import time
from turtle import Screen

from food import Food
from snake import Snake
from score_board import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
snake = Snake()
food = Food()
score_board = Scoreboard()

game_is_on = True
while game_is_on:
    screen.listen()
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.snake_eaten()
        score_board.add_score()
    # if snake.head.distance(0,280)<15 or snake.head.distance(0,-290)<15 or snake.head.distance(0,280)<15

    screen.onkey(snake.right, "Right")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.up, "Up")

screen.exitonclick()
