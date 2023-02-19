from main import *
import matplotlib.pyplot as plt

total=300
plant_list = [1]*int(total*0.7) + [2]*int(total*0.1) + [3]*int(total*0.1) + [4]*int(total*0.1)

plt.figure(dpi=300).set_size_inches(8,6)
x_ax = range(0,301)
world_set = []
for i in range(0,5):
    world_set.append(init_sp(plant_list))
temperature,humidity,_ = simulate_tropical_savanna_climate_daily()
tik=0
while 1:

    climate = Climate(temperature[tik],humidity[tik])
    plants_iteration()
    for section in world.sections:
        sec_itr(section,climate)
    
    world.update_sec()

    tik = tik + 1

    log.append(len(world.plants)/total)
    if tik > 300 or len(world.plants)==0 :
        break
    
    
plt.xlabel("day")
plt.ylabel("survival possibility")
plt.ylim(0,1.05)
plt.xlim(0,300)
plt.savefig("log.png")