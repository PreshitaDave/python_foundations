
Problem 1. Principle Component Analysis

A) Visualize the raw data for all of the points in the 3rd versus the 18th dimensions in the datapoints.csv file.


B) Perform a principle component analysis (PCA) on the data and return all the principle components. Show the principle components in a pandas data-frame.


C) Plot the variance captured by each principal component. Based on this plot, ex- plain if PCA is a good option to reduce the dimensions of the given data.


D) Plot the first two principal components. Make sure to include the variance cap- tured by the first two principal components in the axis labels.




Problem 2. K-Means Clustering

A) Using the principle component data generated from problem 1B, plot the sum of squared distances of all points in a cluster for all principal components (1-20). Please use sklearn’s KMeans method and its attribute kmeans.inertia to obtain the sum of squared distances. From this plot, you should be able to deduce the optimal number of clusters. Please report the optimal number of clusters based on your plot.


B) Perform K-Means clustering using the first two dimensions of the ORIGINAL DATA (data from the datapoints.csv). To determine the number of clusters that you should begin with, refer to your elbow plot from problem 2A, and randomly generate the points of centroids according to that cluster number (i.e. if you reported the optimal number of clusters to be 10 in problem 2A, you should start with 10 centroids). Before generating these centroids, set your random seed as follows: random.seed(10). Perform 10 iterations of K-Means. Finally, plot the K-Means clusters. It should be clear on the plot as to what cluster each point belongs to (i.e. each cluster should be a different color). This plot should also contain the final calculated centroid for each cluster. Make sure to include a legend for your plot.
