# Clustering
# Introduction:

A program that intakes data from one of three CSV files and clusters the data using user input and the K-means algorithm.

# Features:

The Clustering program is able to read CSV file with specific names and extract the data within said files. It then prints the data points as a scatter plot and uses the K-means algorithm to create clusters within the data. The user is allowed to select the number of clusters they would like to see as well as the number of iterations used to properly distinguish each cluster.

# Instructions:

Upon running the program the user is prompted to enter one of three file names: data2008, data1953, or dataBoth. The program will then open the selected file. The file names are case sensitive and the user will be notified if the selection is not valid, in which case they will be prompted to enter the file name again.

After selecting the file the user will be prompted to enter how many clusters they would like to divie the data by. The program currently supports up to 10 different clusters.

The user is then prompted to input how many iterations they would like in order to refine the clusters on certain areas of the data.

After entering all the above information the program will open a scatter plot view with all the file's data points plotted. The dots are the file's data and the + signs are the current cluster means. All dots are color coordinated with their closest cluster means for ease of viewing.

The program will only show one iteration at a time, in order to see the next iteration simply exit the view by click "x" at the top right. After exiting the scatter plot view the program will print the sum of all distances from each point to their respective + signs, this will ensure the program is running correctly and is refining the clusters properly. The program will then open another scatter plot view with the new clusters plotted. The user may continue exiting the view to see each individual iteration as well as the sum of the distances from each point to their respective + signs.

On the final iteration the program will also print the following information for each cluster. The number of countries in the cluster, the mean number of births per 1000 people each year, the mean life expectancy in years, and a list of all the countries in the cluster.

After reviewing the information the user can exit the final scatter plot view and the program will shut down.
