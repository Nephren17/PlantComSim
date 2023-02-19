import pickle
import matplotlib.pyplot as plt

data_set = []
cnt = 0
with open('data1.pkl', 'rb') as f:
    while True:
        try:
            data = pickle.load(f)
            data_set.append(data)
            cnt = cnt + 1
        except EOFError:
            break

print(data_set)
x_ax = range(0,301)

plt.figure(dpi=300).set_size_inches(8,6)
for i in range(0,cnt):
    plt.plot(x_ax,data_set[i],linewidth=3,label="trial"+str(i+1))
plt.legend()
plt.xlabel("day")
plt.ylabel("survival possibility")
plt.ylim(0,1.05)
plt.xlim(0,300)
plt.savefig("set1_record.png")