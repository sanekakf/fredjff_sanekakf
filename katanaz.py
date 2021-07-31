#https://www.ursinaengine.org/documentation.html
#https://www.ursinaengine.org/cheat_sheet_dark.html
from sys import modules
from numpy import positive
from ursina import * 
import time as t
from ursina.prefabs.platformer_controller_2d import PlatformerController2d
from threading import Thread

#Тут поясняется что будет безрамочный режим, а еще позиция фулскрин выключена, можешь попробовать - мне не понравилась
window.borderless = False
# window.fullscreen = True

#Приложение, и текстурка игрока
app = Ursina()
player_texture=load_texture('hero.png')
enemy_texture = load_texture('enemy.png')
#игрок
player = PlatformerController2d(scale_y=1, scale_box=1,max_jumps=2, texture=player_texture, color = color.white)

#модельки
gold_coin= load_texture('gold_coin(angr).png')

#генератор уровня
quad = load_model('quad')
enemy= Entity()
money=Entity()
level_parent = Entity(model=Mesh(vertices=[], uvs=[]), texture='white_cube')
def make_level(texture):
    [destroy(c) for c in level_parent.children]

    for y in range(texture.height):
        collider = None
        for x in range(texture.width):
            col = texture.get_pixel(x,y)
            # print(col)
            #если цвет черный - то это земля(на чем может стоять игрок)
            if col == color.black:
                level_parent.model.vertices += [Vec3(*e) + Vec3(x+.5,y+.5,0) for e in quad.vertices] # copy the quad model, but offset it with Vec3(x+.5,y+.5,0)
                level_parent.model.uvs += quad.uvs
                if not collider:
                    coll = Entity(parent=level_parent, position=(x,y), model='quad', origin=(-.5,-.5), collider='box', visible=False)
                else:
                    collider.scale_x += 1
            else:
                collider = None

            #если цвет зеленый, то объявляется стартовая позиция игрока
            if col == color.green:
                player.start_position = (x, y+3)
                player.position = player.start_position
            
            #если цвет красный, то объявляется враг
            if col == color.red:
                global enemy
                enemy = Entity(model='cube', collider='box', texture=enemy_texture,position=(x,y+.5))

            #если цвет желтый, то тут должен был быть текст - но я хз епт
            if col == color.yellow:
                global money
                money= Entity(model='quad', collider='box', position=(x,y+2), texture=gold_coin, scale_x=2,scale_y=2.5  )

            if col == color.blue:
                global invs
                invs = Entity(parent=level_parent,position=(x,y),model='quad',color=color.cyan,origin=(-.5,-.5), visible=False)
    level_parent.model.generate()
t.sleep(1)

#камера
camera.orthographic = True
camera.position = (30/2,8)
camera.fov = 16

# селектор лвл
def change():
    lvl1.disable()
    lvl2.disable()
    lvl3.disable()
    make_level(load_texture(r'levels\standart.png'))
def change1():
    lvl1.disable()
    lvl2.disable()
    lvl3.disable()
    make_level(load_texture(r'levels\new.png'))
def change3():
    lvl1.disable()
    lvl2.disable()
    lvl3.disable()
    make_level(load_texture(r'levels\big.png'))
    #если уровень большой, то юзаем вот этот пункт с камерой
    camera.add_script(SmoothFollow(target=player, offset=[0,5,-30], speed=4))

lvl1 = Button(scale=(.5,.25),text='Уровень 1')
lvl1.x -= 0.6
lvl2 = Button(scale=(.5,.25), text='Уровень 2')
lvl3 = Button(scale=(.5,.25), text='Уровень 3')
lvl3.x += 0.6
lvl1.on_click = change
lvl2.on_click = change1
lvl3.on_click = change3



player.traverse_target = level_parent
bullets = []
admin=0
#проверяем кнопачки
def input(key):
    if key =='q':
        print('quad')
        app.destroy()
    if key == 'x':
        global bullets
        bullet= Entity(model='cube', color=color.green, position=(player.x,player.y))
        bullets.append(bullet)
    if key == 'c':
        print(bullets)
    if key == 'm':
        #тут при нажатии пяти админов - игрок ресается
        global admin
        admin += 1
        print(admin)
        if admin >= 5:
            player.position = player.start_position


def update():
    # print(bullets)
    for row in bullets:
        row.x =+ 0.1
    #если игрок пересекается с врагом, ресается
    if player.intersects(enemy).hit:
        print('die')
        player.position = player.start_position
    if player.intersects(money).hit:
        player.color = color.gold
        invs.collider = 'box'
        invs.visible = True
    # if player.color == color.gold:

app.run()