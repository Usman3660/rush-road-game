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

app.run()
