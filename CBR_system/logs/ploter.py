import matplotlib.pyplot as plt 

x_labels = []
y = []
limit = 1500
fil = open("log.txt", "r")
for line in fil:
    data = line.split("-")
    x_labels.append( int(data[0]))
    y_value = float((1500-int(data[1])/int(data[0]))*100)
    y.append(y_value)

# print(x_labels[0:limit], y[0:limit])
plt.plot(x_labels[:limit], y[:limit])
plt.show()


# plt.plot(x_labels,y)
# plt.show()