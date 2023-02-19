import numpy as np
from plantclass import *
from world import *
import random
from scipy.spatial import KDTree
import matplotlib.pyplot as plt
import kdtree
from init import *
from waether_sim import simulate_tropical_savanna_climate_daily

world=init(100)
world.vis(line=True)
tik = 0
temperature,humidity,_ = simulate_tropical_savanna_climate_daily()





temp_hp_loss=0
def plant_itr(plant:Plant):
    sec = plant.get_sec()
    temp = temperature[tik]
    hum = humidity[tik]
    k_temp = 1.5
    k_hum = 1
    if temp > plant.t_max:                  #判断温度
        diff = temp - plant.t_max
        plant.hit(diff*k_temp)
        
