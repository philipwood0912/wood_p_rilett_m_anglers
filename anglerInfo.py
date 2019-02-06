import csv
import numpy as np
import matplotlib.pyplot as plt

categories = []

brownYear = []
brownReceived = []
brownHatched = []
rainbowYear = []
rainbowReceived = []
rainbowHatched = []

memberYear = []
memberNumbers = []

dingYear = []
dingFish = []
komoYear = []
komoFish = []
oxboYear = []
oxboFish = []

with open('data/eggs_data.csv') as csvfile:
	reader = csv.reader(csvfile)
	line_count = 0

	for row in reader:
		if line_count is 0:
			print('pushing categories into seperate array')
			categories.append(row)
			line_count += 1
		else:
			nameData = row[0]
			yearData = row[1]
			receivedData = row[2]
			hatchedData = row[3]

			if nameData == "Brown Trout":
				brownYear.append(yearData)
				brownReceived.append(int(receivedData))
				brownHatched.append(int(hatchedData))

			if nameData == "Rainbow Trout":
				rainbowYear.append(yearData)
				rainbowReceived.append(int(receivedData))
				rainbowHatched.append(int(hatchedData))

		line_count += 1

with open('data/member_data.csv') as csvfile:
	reader = csv.reader(csvfile)
	line_count = 0

	for row in reader:
		if line_count is 0:
			print('pushing categories into seperate array')
			categories.append(row)
			line_count += 1
		else:
			yearData = row[0]
			memberData = row[1]

			memberYear.append(yearData)
			memberNumbers.append(int(memberData))

		line_count += 1

with open('data/electro_data.csv') as csvfile:
	reader = csv.reader(csvfile)
	line_count = 0

	for row in reader:
		if line_count is 0:
			print('pushing categories into seperate array')
			categories.append(row)
			line_count += 1
		else:
			nameData = row[0]
			yearData = row[1]
			fishData = row[2]

			if nameData == "Dingman":
				dingYear.append(yearData)
				dingFish.append(int(fishData))

			if nameData == "Komoka":
				komoYear.append(yearData)
				komoFish.append(int(fishData))

			if nameData == "Oxbow":
				oxboYear.append(yearData)
				oxboFish.append(int(fishData))

	line_count += 1


print('processed', line_count, 'lines of data')

members = np.array(memberNumbers)
years = np.array(memberYear)

brownY = np.array(brownYear)
brownR = np.array(brownReceived)
brownH = np.array(brownHatched)

rainbowY = np.array(rainbowYear)
rainbowR = np.array(rainbowReceived)
rainbowH = np.array(rainbowHatched)

fishY = np.array(dingYear)
dingF = np.array(dingFish)
komoF = np.array(komoFish)
oxboF = np.array(oxboFish)

# line graph

fig, ax = plt.subplots()
ax.plot(fishY, dingF, label="Dingman")
ax.plot(fishY, komoF, label="Komoka")
ax.plot(fishY, oxboF, label="Oxbow")

ax.set(xlabel='Years', ylabel='# of Fish Caught',
       title='Rainbow Trout Caught')
ax.grid()

ax.set_xticklabels(fishY, fontsize=10)
ax.legend()

plt.show()

# bar graph

np_eggs = 5
receivedB = (rainbowR)
hatchedB = (rainbowH)
fig, ax = plt.subplots()
index = np.arange(np_eggs)
bar_width = 0.35
opacity = 0.4
error_config = {"ecolor": "0.3"}
rects1 = ax.bar(index, receivedB, bar_width,
                alpha=opacity, color="r",
                error_kw=error_config,
                label="Received")

rects2 = ax.bar(index + bar_width, hatchedB, bar_width,
                alpha=opacity, color="y", 
                error_kw=error_config,
                label="Hatched")

ax.set_xlabel("Years")
ax.set_ylabel("# of Eggs")
ax.set_title("Rainbow Trout Eggs Received vs Hatched")
ax.set_xticks(index + bar_width / 2)
ax.set_xticklabels(("2014", "2015", "2016", "2017", "2018"))
ax.legend()

fig.tight_layout()
plt.show()

#bar chart 2

np_eggs = 5
receivedB = (brownR)
hatchedB = (brownH)
fig, ax = plt.subplots()
index = np.arange(np_eggs)
bar_width = 0.35
opacity = 0.4
error_config = {"ecolor": "0.3"}
rects1 = ax.bar(index, receivedB, bar_width,
                alpha=opacity, color="r",
                error_kw=error_config,
                label="Received")

rects2 = ax.bar(index + bar_width, hatchedB, bar_width,
                alpha=opacity, color="y", 
                error_kw=error_config,
                label="Hatched")

ax.set_xlabel("Years")
ax.set_ylabel("# of Eggs")
ax.set_title("Brown Trout Eggs Received vs Hatched")
ax.set_xticks(index + bar_width / 2)
ax.set_xticklabels(("2014", "2015", "2016", "2017", "2018"))
ax.legend()

fig.tight_layout()
plt.show()

#line graph

m = members
y = years

fig, ax = plt.subplots()
ax.plot(y, m)

ax.set(xlabel='Years', ylabel='TRAA Members',
       title='TRAA Members Over 16 Years')
ax.grid()

ax.set_xticklabels(y, fontsize=7)

plt.show()