from ursina import *
app = Ursina()

from ursina.prefabs.platformer_controller_2d import PlatformerController2d
player = PlatformerController2d(y=1, z=.01, scale_y=1, max_jumps=2)

ground = Entity(model='quad', scale_x=10, collider='box', color=color.black)

quad = load_model('quad')
print('--------------', quad)


level_parent = Entity(model=Mesh(vertices=[], uvs=[]), texture='white_cube')
def make_level(texture):
    [destroy(c) for c in level_parent.children]

    for y in range(texture.height):
        collider = None
        for x in range(texture.width):
            col = texture.get_pixel(x,y)

            if col == color.black:
                level_parent.model.vertices += [Vec3(*e) + Vec3(x+.5,y+.5,0) for e in quad.vertices] # copy the quad model, but offset it with Vec3(x+.5,y+.5,0)
                level_parent.model.uvs += quad.uvs
                if not collider:
                    collider = Entity(parent=level_parent, position=(x,y), model='quad', origin=(-.5,-.5), collider='box', visible=False)
                else:
                    collider.scale_x += 1
            else:
                collider = None

            if col == color.green:
                player.start_position = (x, y)
                player.position = player.start_position

    level_parent.model.generate()

make_level(load_texture('platformer_tutorial_level'))   # generate the level

camera.orthographic = True
camera.position = (30/2,8)
camera.fov = 16



player.traverse_target = level_parent
enemy = Entity(model='cube', collider='box', color=color.red, position=(16,5,-.1))
def update():
    if player.intersects(enemy).hit:
        print('die')
        player.position = player.start_position
def input(key):
    if key =='q':
        print('quad')
        app.destroy()

app.run()