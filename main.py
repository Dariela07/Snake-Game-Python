from turtle import Screen
from snake import Snake
from food import Food
from score import Score
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

screen.listen()  # start listening for keystrokes
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

game_is_on = True
counter = 0
while game_is_on:
    screen.update()
    time.sleep(0.15)
    snake.move()
    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.add_score()

    # Detect collision with wall.
    if snake.head.xcor() > 280 or snake.head.xcor()<-280 or snake.head.ycor()>280 or snake.head.ycor() < -280:
        score.reset()
        snake.reset()
        # game_is_on = False
        # score.game_over()


    # Detect collision with tail.
    # if head collides with any segment in the tail
    # trigger game_over
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            score.reset()
            snake.reset()
            # game_is_on = False
            # score.game_over()

screen.exitonclick()