from ursina import *

app = Ursina()

camera.orthographic = True
camera.fov = 10

window.size = (800, 600)
window.title = "Car Game"
window.borderless = False
window.fullscreen = False

car_speed = 0
obstacle_speed = 0

car = None
road1 = None
road2 = None
obstacles = []
player_score = 0

game_over_text = Text(
    text="GAME OVER",
    origin=(0, 0),
    scale=2,
    color=color.red,
    position=(0, 0.2),
    enabled=False
)

score_text = Text(
    text="Score: 0",
    position=(-0.8, 0.45),
    scale=1.5,
    color=color.white
)

def game_over():
    game_over_text.enabled = True
    game_over_text.animate_scale(3, duration=0.5, curve=curve.out_bounce)
    final_score_text = Text(
        text=f"Final Score: {player_score}",
        scale=2,
        color=color.black,
        position=(-0.5, 0.45), 
    )
    application.pause()

def start_game(difficulty):
    global car_speed, obstacle_speed, car, road1, road2, obstacles, player_score

    player_score = 0
    score_text.text = "Score: 0"

    if difficulty == "easy":
        car_speed = 5
        obstacle_speed = 5
    elif difficulty == "medium":
        car_speed = 8
        obstacle_speed = 8
    elif difficulty == "hard":
        car_speed = 11
        obstacle_speed = 11

    for entity in scene.entities:
        entity.disable()

    car = Entity(
        model='circle',
        color=color.black,
        texture='assets\\car',
        collider='box',
        scale=(2, 1),
        position=(0, -3, 0),
        rotation_z=-90
    )

    road1 = Entity(
        model='quad',
        texture='assets/road',
        scale=15,
        z=1
    )
    road2 = duplicate(road1, y=15)

    obstacles = [
        Entity(
            model='quad',
            texture='red_cube',
            color=color.red,
            collider='box',
            scale=(1.5, 1),
            position=(random.uniform(-4, 4), random.uniform(5, 15), 0)
        ) for _ in range(3)
    ]

def update():
    global player_score

    if not car:
        return

    car.x -= held_keys['a'] * car_speed * time.dt
    car.x += held_keys['d'] * car_speed * time.dt
    car.y += held_keys['w'] * car_speed * time.dt
    car.y -= held_keys['s'] * car_speed * time.dt

    if car.x < -5:
        car.x = -5
    elif car.x > 5:
        car.x = 5
    if car.y < -4:
        car.y = -4
    elif car.y > 4:
        car.y = 4

    for obstacle in obstacles:
        obstacle.y -= obstacle_speed * time.dt
        if obstacle.y < -10:
            obstacle.position = (random.uniform(-4, 4), random.uniform(15, 20), 0)
            player_score += 10
            score_text.text = f"Score: {player_score}"

        if car.intersects(obstacle).hit:
            game_over()

Text("Select Difficulty", origin=(0, 0), scale=2, y=0.3)

Button(
    text="Easy",
    color=color.black,
    scale=(0.3, 0.1),
    position=(-0.5, 0),
    on_click=lambda: start_game("easy")
)

Button(
    text="Medium",
    color=color.black,
    scale=(0.3, 0.1),
    position=(0, 0),
    on_click=lambda: start_game("medium")
)

Button(
    text="Hard",
    color=color.black,
    scale=(0.3, 0.1),
    position=(0.5, 0),
    on_click=lambda: start_game("hard")
)

app.run()
