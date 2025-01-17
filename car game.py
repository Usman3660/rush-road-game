from ursina import *

app = Ursina()

camera.orthographic = True
camera.fov = 10

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
    model ='quad',
    Texture = 'assets\\road',
    scale =15,
    z=1
)

obstacles = [
    Entity(
        model='circle',
        texture='red_cube',
        color=color.red,
        collider='box',
        scale=(1.5, 1),
        position=(random.uniform(-4, 4), random.uniform(5, 15), 0)
    ) for _ in range(3)
]


app.run()
