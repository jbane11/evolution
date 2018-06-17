import numpy 
import random 
import pygame, sys
from pygame.locals import *

global diff_mod
diff_mod =2

def set_diff(diff=1):
    global diff_mod
    if diff != 1 or diff !=2 or diff != 3:
        diff_mod = 2
    diff_mod= diff

class Character:
    '''Defining the atributes(sp) of the Character
        Global varibles include name, health, mana, stamina,skills'''    
    def __init__(self,n='Bob'):
        #type, (if(1) -> size, width of shell....)
        self.dem_info=[1,10,1,1,1]
        #shape 1=circle, 2=elisboid, 3,poloygon
        self.shape=1
        #health, stamina
        #asdsadas
        self.attributes = [1,1,1]
        #strength, elastisty, #bonds, 
        self.charistics = [1,1,1,1,1,1]
        self.velocity = [0,0,0]
        self.name =n
        self.health=10
        self.mana=10
        self.stamin=10
        self.expereince=0
        self.level=1
    def gain_exp(self,a=0):
        self.expereince = self.expereince+a
    def set_level(self,level=1):
        self.level = level
        self.health =10*level
        self.mana = 10*level
        self.stamin=10*level
    def print_status(self,mode=1):
        if mode:
            print("Health:",self.health)
            print("Mana:",self.mana)
            print("Level:",self.level)
            print("Stamina:",self.stamin)
            print("Exp:" ,self.expereince)
        elif mode == 2:
            print("Level:" ,self.level)
            print("Exp:" ,self.expereince)
    def draw_self(self,screen):
        if self.dem_info[0] == 1:
            pygame.draw.circle(screen, [0,0,0],[450,350],self.dem_info[1],self.dem_info[2])
            
    
    
        
class NPC:
    def __init__(self,name="NPC",level=1):
        self.name =name
        self.health=8*level*(diff_mod/2)
        self.mana=8*level*(diff_mod/2)
        self.stamin=8*level*(diff_mod/2)
        self.level=level
        
def Generate_NPC(PC):
    name_str = numpy.loadtxt(fname='/Users/Jason/py_game/evolution/inp/name.csv',dtype=str)
    rand_int = random.randint(0,len(name_str)-1)
    name = name_str[rand_int]
    max_level = PC.level+round(10*diff_mod/3.0)
    min_level = PC.level-13+round(10*diff_mod/3.0)
 
    if min_level <= 0:
        min_level =1
    print(random.randint(min_level,max_level))
    level =random.randint(min_level,max_level) 
    
    NonPC=NPC(name,level)
    return NonPC

class blob:
    def __init__():
        self.name="blob"
        self.dem_info=[1,10,1,1,1]
        #health, stamina, .....
        self.artibutes[1,1,1]
        #strength, elastisty, #bonds, ......
        self.charistics[1,1,1,1,1,1]
        self.velocity[0,0,0]
        self.position[0,0,0]
    def gen_new(PC):
        self.dem_info[1] = PC.dem_info[1]*0.8
            
    def draw(self,screen):
        if self.dem_info[0] == 1:
            pygame.draw.circle(screen, [0,0,0],[450,350],self.dem_info[1],self.dem_info[2])

def Contact(a,b):
    '''Conact between two Characters(class) determines what will happen'''
    if abs(a.level - b.level) < 5:
        winner=Fight(a,b)
    elif a.level > (b.level + 5 ):
        print("No Fight")
    else :
        print("a gets bonus")
        a.gain_exp(b.level-a.level)
        
def Fight(a,b):
    print("Fight")
    a_weight = random.randint(0,11)+a.level
    b_weight = random.randint(0,10)*round(diff_mod/3.0) + b.level
    
    if a_weight > b_weight:
        print("a won")
        exp= (b.level - a.level+6)*10
        a.gain_exp(exp)
#        print("a got",a.level-(b.level-10), "exp")
#        print(a.expereince)
    else :
        print("a lost")
        a.health = a.health - 1*diff_mod
