import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
handler = []
def addPlot(plt, value, color, label):
    red_patch = mpatches.Patch(color=color, label=label)
    handler.append(red_patch)
    plt.legend(handles=handler)
    plt.plot(value, color)
    return plt

# def returnYvalue(filename):
#     y = []
#     limit = 1000
#     fil = open("/home/tartaruz/Dokumenter/NTNU/H2020/ML/Projekt/Code/CBR_system/log/"+filename, "r")
#     for line in fil:
#         data = line.split("-")
#         # print(data)
#         y_value = float(( 1.0-(float(data[1]) / float(data[0])) )*100)
#         y.append(y_value)
    
#     return y[:limit]



# multi_1divDistance = returnYvalue("NewVote_both(w_1divdist).txt")
# multi_eulerDistance = returnYvalue("NewVote_both(w_1diveulerdist).txt")
# multiplication = returnYvalue("NewVote_both(w_multi).txt")

# p = plt

# p = addPlot(p,multi_1divDistance, "blue", "Ratio * W_2")
# p = addPlot(p,multi_eulerDistance, "red", "Ratio * W_1")
# p = addPlot(p,multiplication, "green", "Ratio * Distance")
# p = addPlot(p,[34.5]*1000, "black", "Performance of old voting")


# p.gcf().set_size_inches(15, 6)
# p.xlabel("Quantity of cases tested")
# p.ylabel("Success rate in %")
# p.savefig("./newVote.png", dpi = 300)

f = open("./TheLastTest_retain.txt", "r")
data = [line.replace("\n","").split("-") for line in f]
sum_error = 0
sum_error_array = []
for line in data:
    if line[2]=="1":
        sum_error += 1
    
    sum_error_array.append(line[2])

dev = []
chunk = 1
summen, error = 0,0
print(len(data),int(len(data)/chunk))
for i in range(1,int(len(data)/chunk)):
    start, end = i*chunk, (1+i)*chunk
    for number in sum_error_array[start: end]:
        if number == "0":
            summen += 1
        else:
            error += 1
            summen += 1
    print(error)
    dev.append((error/summen)*100)

print(dev)
p = plt

p = addPlot(p,dev, "blue", "Ratio * W_2")

# p.gcf().set_size_inches(15, 6)
p.xlabel("Quantity of cases tested")
p.ylabel("Success rate in %")

p.show()

print(sum_error/len(data))