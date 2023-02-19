from plantclass import *
from world import *
from typing import List
import math

class Climate:
    def __init__(self,hum,tem) -> None:
        self.hum=0
        self.tem=0
        self.tem_month=0
        self.tem_day=0
        self.rain=0
        self.moist_month=0
        self.moist_day=0
        self.light_month=0
        self.diurnal=0
        pass

def HealthPointIteration(plant:Plant, section:Section, surrounding_Plants:List[Plant]):
    
    # Soil Nutrient
    HP = plant.life + 0.1 * (section.nut)
    
    # Local Temperature
    if plant.t_min > section.tem:
        HP = HP - 10 * (plant.t_min - section.tem)
    elif plant.t_max < section.tem:
        HP = HP + 10 * (plant.t_max - section.tem)

    # Water Point
    if plant.water < 0.6 * plant.water_max:
        HP = HP *(1 - 0.5 * (0.6 * plant.water_max - plant.water) / plant.water_max )


    # Plant to Plant Interaction
    
    for sp in surrounding_Plants:
        if sp.name == "Argy" and plant.name != "Argy":
            HP = HP - 20

    # Environmental damage
    env_dam_reduce = 0
    for sp in surrounding_Plants:
        if sp.name == "Cactus" or sp.name == "Thorn":
            env_dam_reduce = env_dam_reduce + 1
    HP = HP - min (100, 0.1 * HP * (1-(math.atan(env_dam_reduce)*2 / math.pi)*0.5))

    return HP

def WaterPointIteration(plant:Plant, section:Section, surrounding_Plants:List[Plant]):
    
    # Soil Humidity and Surrounding Humidity
    WP = min(plant.water +  0.3 * section.hum, plant.water_max)

    # Local Temperature
    WP = WP - 4 * max(0, section.tem)

    #  Soil Humidity
    desired_total_water = plant.water_max - plant.water
    total_water_max = plant.water_max
    for sp in surrounding_Plants:
        desired_total_water = desired_total_water + sp.water_max - sp.water
        total_water_max = total_water_max + sp.water_max
    if desired_total_water < 0.4 * section.sil_hum:
        WP = plant.water_max
    else:
        WP = plant.water + (plant.water_max / total_water_max) * 0.4 * section.sil_hum

    return WP

#Local(k+1) = Local(k) + Climate->Local + Plant->Local

def SoilHumidityIteration(section:Section, climate:Climate):
    
    # Climate Precipitation
    SH = section.sil_hum + climate.hum//100

    # Reproduction

    # Plant Density
    SH = SH - section.density * 1

    # Climate Temperature
    SH = SH - 4 * max(0, climate.tem - 30)

    # Plant Water Point

    # Plant Function


    return SH