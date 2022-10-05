
Problem 1
Implement a class: binomial_coefficients that computes bi- nomial coefficients using Pascal’s rule. This is the recursion relation, not the formula with factorials. The objects of this class should not recompute the coefficients computed already. This could be useful if the user repeatedly calls the methods of this class. Thus, previously computed values (and possibly some extra values as deemed convenient) should be stored in an internal variable of the object.
The class should have the following public methods:
1. get_n(self, n) should return a list of binomial coefficients for the expansion of the n-th order polynomial (x + y)n, which form the n-th line of Pascal’s triangle. Zeroth line is just 1.
2. get_nk(self, n, k) should return nCk.
3. save_pt(self, n, file_name = 'pascal_triangle.txt')should save the Pascal’s triangle with n+ 1 lines (from 0 to n) in a text file. The triangle should be formatted so that the numbers in the first lines are in the center not on either edge; see the first two figures in the Wikipedia article.


Problem 2
With this problem, we will begin divining into the Human Microbiome Project data. Visit the following webpage: https://hmpdacc.org/hmp/HMQCP/ and download the mapping file for v13 region. Its name should be “v13 map uniquebyPSN.txt”. Write Python scripts to accomplish the following tasks:
1. Determine the number of samples available for just the first visit.
2. For each body site, create a file that contains the ids of the samples from that body site. The file name should contain the name of the body site.
