from plantclass import *
from world import *
from typing import List
import math
import random

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
    HP = plant.life + 0.05 * (section.nut) + random.randint(-65, 6)
    
    # Local Temperature
    if plant.t_min > section.tem:
        HP = HP - 20 * (plant.t_min - section.tem)
    elif plant.t_max < section.tem:
        HP = HP + 20 * (plant.t_max - section.tem)

    # Water Point
    if plant.water < 0.7 * plant.water_max:
        HP = HP + (plant.water - 0.7 * plant.water_max) * 20


    # Plant to Plant Interaction
    
    for sp in surrounding_Plants:
        if sp.name == "Argy" and plant.name != "Argy":
            HP = HP - 20
        if sp.name == "Argy" and plant.name == "Argy":
            HP = HP + 10

    # Environmental damage
    env_dam_reduce = 0
    for sp in surrounding_Plants:
        if sp.name == "Cactus" or sp.name == "Thorn":
            env_dam_reduce = env_dam_reduce + 1
    HP = HP - max (20, 0.05 * HP * (1-(math.atan(env_dam_reduce)*2 / math.pi)*0.5))


    return HP

def WaterPointIteration(plant:Plant, section:Section, surrounding_Plants:List[Plant]):

    # Soil Humidity and Surrounding Humidity
    WP = plant.water - random.randint(-300, 0)
    # Daily Consumption
    WP = WP - plant.water_consume *100

    # Local Temperature
    WP = WP - 400 * max(0, section.tem)

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

    return max(WP, 0)

#Local(k+1) = Local(k) + Climate->Local + Plant->Local

def SoilHumidityIteration(section:Section, climate:Climate):
    
    # Climate Precipitation
    SoH = section.sil_hum + climate.hum//100

    # Reproduction


    # Climate Temperature
    SoH = SoH - 40 * max(0, climate.tem - 10)

    # Plant Water Point
    desired_total_water = 0
    for sp in section.plants:
        desired_total_water = desired_total_water + sp.water_max - sp.water
    SoH = SoH - min(0.4 * section.sil_hum, desired_total_water)

    # Plant Function
    for sp in section.plants:
        if (sp.name == "Locust" or sp.name == "Poplar") and section.sil_hum < 6000:
            SoH = SoH + 0.04 * sp.water

    return SoH

def SurroundingHumidityIteration(section:Section, climate:Climate):
    
    # Climate Precipitations
    SuH = section.hum + 0.15 * climate.hum
    
    # Plant Density
    SuH = SuH * (1 - 0.5 * (2 / math.pi) * math.atan(section.density / 100000))

    # Climate Humidity
    SuH = 0.9 * SuH + 0.1 * climate.hum

    return SuH

def SoilNutrientIteration(section:Section, climate:Climate):
    # Plant Death

    # Plant Reproduction

    # Plant consumption
    SN = SN * (1- 0.4 * (2 / math.pi) * math.atan(section.density / 3000))

    #Plant Function
    for sp in section.plants:
        if sp.name == "Locust" or sp.name == "Stipa":
            SN = SN + 0.3 * sp.life

    # Daily Complement
    SN = SN + 1000
    
    return SN


def spawn(plant:Plant):
    dx = random.uniform(-1,1)*10
    dy = random.uniform(-1,1)*10
    while plant.x + dx > 100 or plant.x + dx < 0 or plant.y + dy > 100 or plant.y + dy <0:
        dx = random.uniform(-1,1)*10
        dy = random.uniform(-1,1)*10
    if plant.name == "Cactus":
        newplant = Cactus(plant.x + dx,plant.y + dy)
    elif plant.name == "Hippophae":
        newplant = Hippophae(plant.x + dx,plant.y + dy)
    elif plant.name == "Thorn":
        newplant = Thorn(plant.x + dx,plant.y + dy)
    elif plant.name == "Stipa":
        newplant = Stipa(plant.x + dx,plant.y + dy)
    elif plant.name == "Villous_themeda":
        newplant = Villous_themeda(plant.x + dx,plant.y + dy)
    elif plant.name == "Arteannuin":
        newplant = Arteannuin(plant.x + dx,plant.y + dy)
    elif plant.name == "Poplar":
        newplant = Poplar(plant.x + dx,plant.y + dy)
    elif plant.name == "Argy":
        newplant = Argy(plant.x + dx,plant.y + dy)
    elif plant.name == "Crofton_weed":
        newplant = Crofton_weed(plant.x + dx,plant.y + dy)
    elif plant.name == "Leymus_chinensis":
        newplant = Leymus_chinensis(plant.x + dx,plant.y + dy)
    elif plant.name == "Locust":
        newplant = Locust(plant.x + dx,plant.y + dy)
    elif plant.name == "Chinese_pennisetum":
        newplant = Chinese_pennisetum(plant.x + dx,plant.y + dy)
    elif plant.name == "Conyza_canadensis":
        newplant = Conyza_canadensis(plant.x + dx,plant.y + dy)
    else:
        newplant = Cactus(plant.x + dx,plant.y + dy)

    newplant.age = 0
    return newplant
