from scene import Scene
import taichi as ti
from taichi.math import *

scene = Scene(voxel_edges=0, exposure=1.0);scene.set_floor(-0.05, (0.957, 0.586, 0.664))
scene.set_background_color((0.942, 0.578, 0.512));scene.set_directional_light((1, 1, 1), 0.2, (1, 0.8, 0.6))

@ti.func
def set_blocks(st, ed, kd, color):
    for I in ti.grouped(ti.ndrange((st[0], ed[0]), (st[1], ed[1]),(st[2], ed[2]))):
        scene.set_voxel(I, kd, color)

@ti.func
def set_lamp(x,y,z):
    col_pil3,col_s,col_l=vec3(0.211,0.211,0.211),vec3(0.793,0.105,0.270),vec3(0.980,0.883,0.316)
    set_blocks(vec3(x,y-8,z),vec3(x+1,y,z+1),1,col_pil3);set_blocks(vec3(x-1,y-9,z-1),vec3(x+2,y-8,z+2),1,col_s)
    set_blocks(vec3(x-2,y-9,z-1),vec3(x+3,y-8,z+2),2,col_l);set_blocks(vec3(x-1,y-9,z-2),vec3(x+2,y-8,z+3),2,col_l)
    set_blocks(vec3(x-3,y-14,z-1),vec3(x+4,y-9,z+2),1,col_s);set_blocks(vec3(x-1,y-14,z-3),vec3(x+2,y-9,z+4),1,col_s)
    set_blocks(vec3(x-2,y-14,z-2),vec3(x+3,y-9,z+3),1,col_s);set_blocks(vec3(x-3,y-11,z-1),vec3(x+4,y-10,z+2),2,col_l)
    set_blocks(vec3(x-1,y-11,z-3),vec3(x+2,y-10,z+4),2,col_l);set_blocks(vec3(x-2,y-11,z-2),vec3(x+3,y-10,z+3),2,col_l)
    set_blocks(vec3(x-3,y-13,z-1),vec3(x+4,y-12,z+2),2,col_l);set_blocks(vec3(x-1,y-13,z-3),vec3(x+2,y-12,z+4),2,col_l)
    set_blocks(vec3(x-2,y-13,z-2),vec3(x+3,y-12,z+3),2,col_l);set_blocks(vec3(x-1,y-16,z-1),vec3(x+2,y-15,z+2),1,col_s)
    set_blocks(vec3(x-2,y-15,z-1),vec3(x+3,y-14,z+2),2,col_l);set_blocks(vec3(x-1,y-15,z-2),vec3(x+2,y-14,z+3),2,col_l)
    set_blocks(vec3(x,y-19,z),vec3(x+1,y-15,z+1),2,vec3(1,1,1))

@ti.kernel
def initialize_voxels():
    col_ground,col_fence,col_pil2=vec3(0.723,0.532,0.488),vec3(0.621,0.207,0.227),vec3(0.555, 0.207, 0.289)
    set_blocks(vec3(-37,-1,-37),vec3(37,0,37),1,col_ground);set_blocks(vec3(-7,-3,38),vec3(7,-2,41),1,col_ground)
    for i in ti.static(range(-32,32,6)):set_blocks(vec3(-37,-1,i),vec3(37,0,i+1),0,col_ground)
    set_blocks(vec3(33,2,-36),vec3(35,4,36),1,col_fence);set_blocks(vec3(33,7,-36),vec3(35,9,36),1,col_fence)
    for i in ti.static(range(-36,36,4)):set_blocks(vec3(33,2,i),vec3(34,7,i+1),1,col_fence)
    set_blocks(vec3(-35,2,-36),vec3(-33,4,36),1,col_fence);set_blocks(vec3(-35,7,-36),vec3(-33,9,36),1,col_fence)
    for i in ti.static(range(-36,36,4)):set_blocks(vec3(-34,2,i),vec3(-33,7,i+1),1,col_fence)
    set_blocks(vec3(-36,2,-35),vec3(36,4,-33),1,col_fence);set_blocks(vec3(-36,7,-35),vec3(36,9,-33),1,col_fence)
    for i in ti.static(range(-36,36,4)):set_blocks(vec3(i,2,-34),vec3(i+1,7,-33),1,col_fence)
    set_blocks(vec3(-36,2,33),vec3(36,4,35),1,col_fence);set_blocks(vec3(-36,7,33),vec3(36,9,35),1,col_fence)
    for i in ti.static(range(-36,36,4)):set_blocks(vec3(i,2,33),vec3(i+1,7,34),1,col_fence)
    set_blocks(vec3(-15,2,33),vec3(15,9,35),0,col_fence);set_blocks(vec3(-1,57,-1),vec3(1,58,1),2,vec3(1,1,1))
    col_pil1,col_wall,col_top=vec3(0.336,0.246,0.180),vec3(0.840, 0.723, 0.555),vec3(0.934,0.730,0.141)
    set_blocks(vec3(33,-4,33),vec3(36,9,36),1,col_pil1);set_blocks(vec3(33,-4,-36),vec3(36,9,-33),1,col_pil1)
    set_blocks(vec3(-36,-4,33),vec3(-33,9,36),1,col_pil1);set_blocks(vec3(-36,-4,-36),vec3(-33,9,-33),1,col_pil1)
    set_blocks(vec3(-18,0,33),vec3(-15,9,36),1,col_pil1);set_blocks(vec3(15,0,33),vec3(18,9,36),1,col_pil1)
    set_blocks(vec3(-18,0,-18),vec3(18,38,18),1,col_wall);set_blocks(vec3(-17,0,-17),vec3(17,38,17),0,col_wall)
    col_gunjo=vec3(0.316,0.656,0.863);set_blocks(vec3(-18,10,-7),vec3(18,25,7),0,col_wall)
    set_blocks(vec3(16,0,16),vec3(20,38,20),1,col_pil2);set_blocks(vec3(-20,0,16),vec3(-16,38,20),1,col_pil2)
    set_blocks(vec3(16,0,-20),vec3(20,38,-16),1,col_pil2);set_blocks(vec3(-20,0,-20),vec3(-20,38,-20),1,col_pil2)
    set_blocks(vec3(7,0,16),vec3(11,38,20),1,col_pil2);set_blocks(vec3(-11,0,16),vec3(-7,38,20),1,col_pil2)
    set_blocks(vec3(7,0,-20),vec3(11,38,-16),1,col_pil2);set_blocks(vec3(-11,0,-20),vec3(-7,38,-16),1,col_pil2)
    set_blocks(vec3(16,0,7),vec3(20,38,11),1,col_pil2);set_blocks(vec3(16,0,-11),vec3(20,38,-7),1,col_pil2)
    set_blocks(vec3(-20,0,7),vec3(-16,38,11),1,col_pil2);set_blocks(vec3(-20,0,-11),vec3(-16,38,-7),1,col_pil2)
    set_blocks(vec3(-19,25,-19),vec3(19,28,19),1,col_pil2);set_blocks(vec3(-16,25,-16),vec3(16,28,16),0,col_pil2)
    set_blocks(vec3(-19,7,-19),vec3(19,10,19),1,col_pil2);set_blocks(vec3(-16,7,-16),vec3(16,10,16),0,col_pil2)
    set_blocks(vec3(-7,0,-20),vec3(7,25,20),0,vec3(0.840, 0.723, 0.555))
    for i in ti.static(range(-18,18,7)):
        set_blocks(vec3(i,35,-28),vec3(i+3,38,28),1,col_pil2);set_blocks(vec3(-28,35,i),vec3(28,38,i+3),1,col_pil2)
    for i in ti.static(range(2,7,2)):
        set_blocks(vec3(17,10,i-1),vec3(18,25,i),1,col_pil2);set_blocks(vec3(17,10,-i),vec3(18,25,-i+1),1,col_pil2)
        set_blocks(vec3(-18,10,i-1),vec3(-17,25,i),1,col_pil2);set_blocks(vec3(-18,10,-i),vec3(-17,25,-i+1),1,col_pil2)
    for i in ti.static(range(12,25,4)):
        set_blocks(vec3(18,i,-7),vec3(19,i+2,7),1,col_pil2);set_blocks(vec3(-19,i,-7),vec3(-18,i+2,7),1,col_pil2)
    for i in ti.static(range(0,3)):
        set_blocks(vec3(-(25+i*3),38+i,-(25+i*3)),vec3(25+i*3,39+i,25+i*3),1,col_gunjo)
    for i in ti.static(range(0,6)):
        set_blocks(vec3(-(35-i*3),41+i,-(35-i*3)),vec3(35-i*3,42+i,35-i*3),1,col_gunjo)
        set_blocks(vec3((32-i*3),41+i,(32-i*3)),vec3((35-i*3),43+i,(35-i*3)),1,col_gunjo)
        set_blocks(vec3(-(35-i*3),41+i,(32-i*3)),vec3(-(32-i*3),43+i,(35-i*3)),1,col_gunjo)
        set_blocks(vec3((32-i*3),41+i,-(35-i*3)),vec3((35-i*3),43+i,-(32-i*3)),1,col_gunjo)
        set_blocks(vec3(-(35-i*3),41+i,-(35-i*3)),vec3(-(32-i*3),43+i,-(32-i*3)),1,col_gunjo)
        for j in ti.static(range(-13,13,8)):
            set_blocks(vec3(j,41+i,(34-i*3)),vec3(j+2,43+i,(37-i*3)),1,col_gunjo)
            set_blocks(vec3(j,41+i,-(37-i*3)),vec3(j+2,43+i,-(34-i*3)),1,col_gunjo)
            set_blocks(vec3((34-i*3),41+i,j),vec3((37-i*3),43+i,j+2),1,col_gunjo)
            set_blocks(vec3(-(37-i*3),41+i,j),vec3(-(34-i*3),43+i,j+2),1,col_gunjo)
    for i in ti.static(range(0,4)):
        set_blocks(vec3((33+i),41+i,(33+i)),vec3((35+i),43+i,(35+i)),1,col_gunjo)
        set_blocks(vec3(-(35+i),41+i,(33+i)),vec3(-(33+i),43+i,(35+i)),1,col_gunjo)
        set_blocks(vec3((33+i),41+i,-(35+i)),vec3((35+i),43+i,-(33+i)),1,col_gunjo)
        set_blocks(vec3(-(35+i),41+i,-(35+i)),vec3(-(33+i),43+i,-(33+i)),1,col_gunjo)
    set_blocks(vec3(-1,47,-1),vec3(1,57,1),1,col_top);set_blocks(vec3(-5,47,-5),vec3(5,48,5),1,col_top)
    set_blocks(vec3(-2,49,-2),vec3(2,50,2),1,col_top);set_blocks(vec3(-2,51,-2),vec3(2,52,2),1,col_top)
    set_blocks(vec3(-2,54,-1),vec3(2,56,1),1,col_top);set_blocks(vec3(-1,54,-2),vec3(1,56,2),1,col_top)
    set_lamp(31,41,31);set_lamp(-31,41,31);set_lamp(31,41,-31);set_lamp(-31,41,-31)
    col_torii,col_black=vec3(0.938,0.254,0.332),vec3(0.043,0.063,0.074)
    set_blocks(vec3(-20,-4,60),vec3(-18,50,62),1,col_torii);set_blocks(vec3(18,-4,60),vec3(20,50,62),1,col_torii)
    set_blocks(vec3(-22,43,60),vec3(22,45,62),1,col_torii);set_blocks(vec3(-26,50,60),vec3(26,52,62),1,col_torii)
    set_blocks(vec3(-28,52,60),vec3(28,53,62),1,col_black);set_blocks(vec3(-30,53,60),vec3(30,54,62),1,col_black)
    set_blocks(vec3(-2,45,60),vec3(2,50,62),1,col_torii)

initialize_voxels()

scene.finish()