import pickle
import matplotlib.pyplot as plt

data_set = []
cnt = 0
with open('data_d.pkl', 'rb') as f:
    while True:
        try:
            data = pickle.load(f)
            data_set.append(data)
            cnt = cnt + 1
        except EOFError:
            break

print(data_set)
x_ax = range(0,1001)

plt.figure(dpi=300).set_size_inches(10,6)

plt.plot(x_ax,data_set[3],linewidth=2,label="biodiversity-1")
plt.plot(x_ax,data_set[1],linewidth=2,label="biodiversity-2")
plt.plot(x_ax,data_set[0],linewidth=2,label="biodiversity-3")
plt.plot(x_ax,data_set[2],linewidth=2,label="biodiversity-4")

plt.legend(bbox_to_anchor=(0.92, 1), loc='upper left')
plt.xlabel("day")
plt.ylabel("survival chance")
plt.title("plant communities with different biodiversity")
plt.ylim(0,)
plt.xlim(0,)
plt.savefig("log_d.png")