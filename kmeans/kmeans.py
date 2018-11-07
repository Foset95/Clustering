import pandas as pd
import numpy as np
import csv
import matplotlib.pyplot as plt
import random

#Determines the distance between 2 (x,y) coordinates
def euclid(point1_x, point1_y, point2_x, point2_y):
    return np.sqrt((point1_x-point2_x)**2+(point1_y-point2_y)**2)

#Reading the csv files and putting them into a dataframe
valid_select = False
data = []
while(valid_select == False):
    file = input("Which file would you like to load: data2008, data1953, or dataBoth? ")
    type(file)
    if(file == "data2008"):
        with open("data2008.csv", 'r') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            next(reader)
            for row in reader:
                data.append(row)
            df = pd.DataFrame(data, columns=["Country", "x", "y"])
            df["x"], df["y"] = df["x"].astype(float), df["y"].astype(float)
        valid_select = True
    elif(file == "data1953"):
        with open("data1953.csv", 'r') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            next(reader)
            for row in reader:
                data.append(row)
            df = pd.DataFrame(data, columns=["Country", "x", "y"])
            df["x"], df["y"] = df["x"].astype(float), df["y"].astype(float)
        valid_select = True
    elif(file == "dataBoth"):
        with open("dataBoth.csv", 'r') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            next(reader)
            for row in reader:
                data.append(row)
            df = pd.DataFrame(data, columns=["Country", "x", "y"])
            df["x"], df["y"] = df["x"].astype(float), df["y"].astype(float)
        valid_select = True
    else:
        print("I'm sorry, that isn't a valid selection")

#Determining the number of clusters and iterations
clusters = int(input("How many clusters would you like for the data? "))
type(clusters)
iters = int(input("How many iterations would you like for the data? "))
type(iters)

#Getting the starting centroid coordinates
centroids = []
index = random.sample(range(196), clusters)
for i in range(clusters):
    centroids.append(df["x"][index[i]])
    centroids.append(df["y"][index[i]])
centroids = np.reshape(centroids, (clusters, 2))

#Creating the color map
colors = ['black', 'blue', 'orange', 'red', 'green', 'magenta', 'yellow', 'cyan', 'purple', 'lime']
colmap = {}
for i in range(clusters):
    colmap[i] = colors[i]

#Color assigner
def assigner(df, centroids):
    distances = []
    for i in range(len(centroids)):
        for x in range(len(df)):
            distances.append(euclid(df["x"][x], df["y"][x], centroids[i][0], centroids[i][1]))
            df[i] = pd.Series(distances)
        distances = []

    closest = []
    for i in range(len(df)):
        min_col = df[0][i]
        for x in range(1, len(centroids)):
            min_col = np.min((min_col, df[x][i]))
        closest.append(df.iloc[i].eq(min_col).idxmax())
    df["closest"] = pd.Series(closest)

#Plotting the points and assigning colors
total_dist = 0
for i in range(iters):
    plt.ylabel("Life Expectancy in Years")
    plt.xlabel("Births per 1000 People Each Year")
    if(i == 0):
        assigner(df, centroids)
        for x in range(len(centroids)):
            plt.scatter(centroids[x][0], centroids[x][1], marker='+', s=150, c=colmap[x])
        for x in range(len(df)):
            plt.scatter(df["x"][x], df["y"][x], marker='.', c=colmap[df["closest"][x]])
        plt.show()
        for y in range(len(centroids)):
            for z in range(len(df)):
                if(df["closest"][z] == y):
                    total_dist = total_dist + df[y][z]
        print("Sum of all distances from each point to its cluster mean: ", total_dist)
        total_dist = 0
    elif(i > 0) and (i < iters-1):
        meanx, meany, count = 0, 0, 0
        for x in range(len(centroids)):
            for y in range(len(df)):
                if(df["closest"][y] == x):
                    count = count + 1
                    meanx = meanx + df["x"][y]
                    meany = meany + df["y"][y]
            centroids[x][0] = meanx/count
            centroids[x][1] = meany/count
            count, meanx, meany = 0, 0, 0
        assigner(df, centroids)
        for x in range(len(centroids)):
            plt.scatter(centroids[x][0], centroids[x][1], marker='+', s=150, c=colmap[x])
        for x in range(len(df)):
            plt.scatter(df["x"][x], df["y"][x], marker='.', c=colmap[df["closest"][x]])
        plt.show()
        for y in range(len(centroids)):
            for z in range(len(df)):
                if(df["closest"][z] == y):
                    total_dist = total_dist + df[y][z]
        print("Sum of all distances from each point to its cluster mean: ", total_dist)
        total_dist = 0
    else:
        count_list = []
        meanx, meany, count = 0, 0, 0
        for x in range(len(centroids)):
            for y in range(len(df)):
                if(df["closest"][y] == x):
                    count = count + 1
                    meanx = meanx + df["x"][y]
                    meany = meany + df["y"][y]
            centroids[x][0] = meanx/count
            centroids[x][1] = meany/count
            count, meanx, meany = 0, 0, 0
            assigner(df, centroids)
        for x in range(len(centroids)):
            plt.scatter(centroids[x][0], centroids[x][1], marker='+', s=150, c=colmap[x])
        for x in range(len(df)):
            plt.scatter(df["x"][x], df["y"][x], marker='.', c=colmap[df["closest"][x]])
        for x in range(len(centroids)):
            for y in range(len(df)):
                if(df["closest"][y] == x):
                    count = count + 1
                    meanx = meanx + df["x"][y]
                    meany = meany + df["y"][y]
            centroids[x][0] = meanx/count
            centroids[x][1] = meany/count
            count_list.append(count)
            count, meanx, meany = 0, 0, 0
            print("The number of countries in cluster {} are:".format(x+1))
            print(count_list[x])
            print()
            
            print("The mean number of births per 1000 people each year in cluster {} is:".format(x+1))
            print(centroids[x][0])
            print()

            print("The mean life expectancy in years in cluster {} is:".format(x+1))
            print(centroids[x][1])
            print()

            print("Here is a list of all the countries in cluster {}:".format(x+1))
            for y in range(len(df)):
                if(df["closest"][y] == x):
                    print(df["Country"][y])
            print()
        plt.show()
        for y in range(len(centroids)):
            for z in range(len(df)):
                if(df["closest"][z] == y):
                    total_dist = total_dist + df[y][z]
        print("Sum of all distances from each point to its cluster mean: ", total_dist)
        total_dist = 0





