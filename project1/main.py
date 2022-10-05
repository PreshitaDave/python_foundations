######################
#Group members:
#Adalee Koshiol
#Srija Chillamcherla
#Preshita Dave
#Manas Dhanuka
######################


class array:
    def __init__(self, array):
        '''The constructor function should give objects of this class several attributes: size, shape, and data.'''
        #initialize counters for entries and rows
        entries = 0
        rows = 0
        #iterate through the array
        #if the first item in the array is a list, iterate through it like a matrix
        if type(array[0]) == list:
            for i in range(len(array)):
                #for each list in the array, add 1 to the row counter
                rows += 1
                for j in range(len(array[i])):
                    #for each value within the lists in the array, add 1 to the entries counter
                    entries += 1
            #the number of columns is the entries divided by the number of rows
            cols = int(entries/rows)
        #otherwise its a 1D array, so iterate through it as a list
        else:
            for i in range(len(array)):
                #for each value in the list, add one to the entries counter
                entries += 1
            #for a 1D array, the number of rows will always be 1
            rows = 1
            #and the number of columns will always be the number of entries
            cols = entries
        #define the attributes given the counters
        self.size = entries
        self.shape = (rows, cols)
        self.data = array
    def transpose(self):
        '''This method should return a new array object with the rows and columns reversed.'''
        #unpack the tuple of rows and columns from the shape attribute
        r, c = self.shape
        #initalize an empty array to put the transposed array into
        trans_arr = []
        #if the rows are greater than 1, it is a 2D array
        if r > 1:
            if c > 1:
                #make the transposed array have the correct number of rows (which is the number of original columns)
                for i in range(c):
                    trans_arr.append([])
                #make the transposed array have the correct number of columns (which is the number of original rows)
                for j in range(len(trans_arr)):
                    for k in range(r):
                        #put zeros in to keep it an empty array
                        trans_arr[j].append(0)
                #change out the zeros for original data
                for i in range(len(self.data)):
                    for j in range(len(self.data[0])):
                        trans_arr[j][i] = self.data[i][j]
            elif c == 1:
                for i in range(r):
                    for j in range(c):
                        trans_arr.append(self.data[i][j])
        #if the rows are equal to 1, it is a 1D array
        elif r == 1:
            for i in range(len(self.data)):
                trans_arr.append([self.data[i]])
        #return the transposed array
        return trans_arr
    def sum(self, sum_type = 2):
        '''This method should sum all the elements in the array. If the sum_type argument is specified, 0 will give
        the sum along the rows, and 1 will give the sum along the columns. The sum along the rows will be
        returned as a row vector, and the sum along the columns will be returned as a column vector.
        If no sum_type argument is specified, the argument will be left at 2 and give the sum of all the 
        entries in the array.'''
        r, c = self.shape
        #if the sum_type is left at 2, then give the sum for all the entries in the array
        if sum_type == 2:
            arr_sum = 0
            #check to see if it is a 2D array
            if type(self.data[0]) == list: 
                #iterate through the rows in the array
                for i in range(len(self.data)):
                    #iterate through the columns in the array
                    for j in range(len(self.data[i])):
                        #add what's in that position to the sum
                        arr_sum += self.data[i][j]
            else:
                for i in range(len(self.data)):
                    arr_sum += self.data[i]
        #if the sum_type is changed to 1, then give the sum for each column in a row vector
        elif sum_type == 1:
            #check to see if it is a 2D array
            if type(self.data[0]) == list:
                if c > 1:
                    #make the array into an array object to transpose it
                    arr = array(self.data)
                    tr = arr.transpose()
                    col_sum = 0
                    arr_sum = []
                    #do the same process of row sums but since it's transposed, it does the columns
                    for i in range(len(tr)):
                        for j in range(len(tr[i])):
                            col_sum += tr[i][j]
                        arr_sum.append(col_sum)
                        col_sum = 0
                elif c == 1:
                    temp_sum = 0
                    for i in range(len(self.data)):
                        for j in range(len(self.data[i])):
                             temp_sum += self.data[i][j]
                    arr_sum = [temp_sum]
            else:
                arr_sum = self.data
        #if the sum_type is changed to 0, then give the sum for each row in a column vector
        elif sum_type == 0:
            arr_sum = []
            #check to see if it is a 2D array
            if type(self.data[0]) == list:
                row_sum = 0
                #iterate through each row
                for i in range(r):
                    #iterate through each element in the row
                    for j in range(c):
                        #add each element to each other
                        row_sum += self.data[i][j]
                    #append the sum list with a list of the row sum
                    arr_sum.append([row_sum])
                    #reset the row_sum for the next row sum
                    row_sum = 0
            #if it's not 2D, it's 1D
            else:
                row_sum = 0
                #iterate through each element in the list
                for i in range(len(self.data)):
                    #add the elements to each other
                    row_sum += self.data[i]
                #append the array sum list with the final row sum
                arr_sum.append([row_sum])
        #return the appropriate array of sums
        return arr_sum
    def __add__(self, B):
        '''This method will overload the addition operator allowing arrays to be added 
        element-wise together using the + operation. It supports addition by scalars 
        (as integers or floats) as well as arrays of the same shape.
        
        Parameters
        ----------
        B : int, float, array, nested list
        
        Returns
        -------
        added_arr : array'''
        #make a copy of the self array to get an array of the same shape
        r, c = self.shape
        added_arr = [[0]*c for i in range(r)]
        #when adding an integer to the array
        if type(B) == int or type(B) == float:
            #if the number of rows is great than 1, it is a 2D array
            if r > 1:
                #iterate through each element of the array
                for i in range(r):
                    for j in range(c):
                        #add the integer to each element in the array
                        added_arr[i][j] = self.data[i][j] + B
            #if the number of rows is 1, then it is a 1D array
            elif r == 1:
                added_arr = added_arr[0]
                #iterate through the list/array
                for i in range(len(added_arr)):
                    #add the integer
                    added_arr[i] = self.data[i] + B
        #when adding a nested list to an array
        elif type(B) == list:
            B_arr = array(B)
            if B_arr.shape == self.shape:
              #if the self array has rows greater than 1, it is a 2D array
              if r > 1:
                for i in range(len(self.data)):
                    for j in range(len(self.data[i])):
                        added_arr[i][j] = self.data[i][j] + B_arr.data[i][j]
              #if the self array has rows = 1, it is a 1D array (a list)
              elif r == 1:
                added_arr = added_arr[0]
                for i in range(len(added_arr)):
                    added_arr[i] = self.data[i] + B_arr.data[i]
            else:
                added_arr = "Error: Arrays must be the same size"
        #when adding an array to an array
        elif type(B.data) == list:
            #if the shapes are the same, we can add them together
            if B.shape == self.shape:
              #if the self array has rows greater than 1, it is a 2D array
              if r > 1:
                for i in range(len(self.data)):
                    for j in range(len(self.data[i])):
                        added_arr[i][j] = self.data[i][j] + B.data[i][j]
              #if the self array has rows = 1, it is a 1D array (a list)
              elif r == 1:
                added_arr = added_arr[0]
                for i in range(len(added_arr)):
                    added_arr[i] = self.data[i] + B.data[i]
            else:
                added_arr = "Error: Arrays must be the same size"
        #return the sum of the two arrays
        return added_arr
    def __mul__(self, B):
        '''
        This method overloads the multiplication operator to perform element-wise multiplication on an array. It supports multiplication by scalars (integers or floats) as well as arrays of the same size.

        Parameters
        ----------
        B : int, float, array, nested list
        
        Returns
        -------
        mult_arr : array
        '''
        #make a copy of the self array to get an array of the same shape
        r, c = self.shape
        mult_arr = [[0] * c for i in range(r)] 
        #multiplying an integer or a float to an array 
        if type(B) == int or type(B) == float:
            #if the number of rows greater than 1, it's a 2D array or column vector
            if r > 1:
                # iterate through each element of the array 
                for i in range(r):
                    for j in range(c):
                        mult_arr[i][j] = self.data[i][j] * B
            # for a 1D array 
            elif r == 1:
                mult_arr = mult_arr[0]
                #iterate through 1D array 
                for i in range(len(mult_arr)):
                    mult_arr[i] = self.data[i] * B
        #when multiplying a nested list with an array
        elif type(B) == list:
            B_arr = array(B)
            if B_arr.shape == self.shape:
                #for a 2D array
                if r > 1:
                    for i in range(len(self.data)):
                        for j in range(len(self.data[i])):
                            mult_arr[i][j] = self.data[i][j] * B_arr.data[i][j]
                #if the self array has one row, it's a 1D array 
                elif r == 1:
                    mult_arr = mult_arr[0]
                    for i in range(len(self.data)):
                        mult_arr[i] = self.data[i] * B_arr.data[i]
            else:
                mult_arr = "Error: Arrays must be the same size"
        #multiplying an array with an array
        elif type(B.data) == list:
            if B.shape == self.shape:
                #for a 2D array
                if r > 1:
                    for i in range(len(self.data)):
                        for j in range(len(self.data[i])):
                            mult_arr[i][j] = self.data[i][j] * B.data[i][j]
                #if the self array has one row, it's a 1D array 
                elif r == 1:
                    mult_arr = mult_arr[0]
                    for i in range(len(self.data)):
                        mult_arr[i] = self.data[i] * B.data[i]
            else:
                mult_arr = "Error: Arrays must be the same size"
        return mult_arr
    def __sub__(self, B):
        '''
        This method overloads the subtraction operator to perform element-wise subtraction on an array. It supports subtraction by scalars (integers or floats) as well as arrays of the same size.

        Parameters
        ----------
        B : int, float, array, nested list
        
        Returns
        -------
        sub_arr : array
        '''
        #make a copy of the self array to get an array of the same shape
        r, c = self.shape
        sub_arr = [[0] * c for i in range(r)] 
        #subtracting an integer or a float from an array 
        if type(B) == int or type(B) == float:
            #if the number of rows greater than 1, it's a 2D array or column vector
            if r > 1:
                #iterate through each element of the array 
                for i in range(r):
                    for j in range(c):
                        sub_arr[i][j] = self.data[i][j] - B
            #for a 1D array 
            elif r == 1:
                sub_arr = sub_arr[0]
                #iterate through 1D array 
                for i in range(len(sub_arr)):
                    sub_arr[i] = self.data[i] - B
        #subtracting a nested list and an array
        elif type(B) == list:
            B_arr = array(B)
            if B_arr.shape == self.shape:
                #for a 2D array
                if r > 1:
                    for i in range(len(self.data)):
                        for j in range(len(self.data[i])):
                            sub_arr[i][j] = self.data[i][j] - B_arr.data[i][j]
                #if the self array has one row, it's a 1D array 
                elif r == 1:
                    sub_arr = sub_arr[0]
                    for i in range(len(self.data)):
                        sub_arr[i] = self.data[i] - B_arr.data[i]
            else:
                sub_arr = "Error: Arrays must be the same size"            
        #when subtracting an array and an array
        elif type(B.data) == list:
            if B.shape == self.shape:
                #for a 2D array
                if r > 1:
                    for i in range(len(self.data)):
                        for j in range(len(self.data[i])):
                            sub_arr[i][j] = self.data[i][j] - B.data[i][j]
                #if the self array has one row, it's a 1D array 
                elif r == 1:
                    sub_arr = sub_arr[0]
                    for i in range(len(self.data)):
                        sub_arr[i] = self.data[i] - B.data[i]
            else:
                sub_arr = "Error: Arrays must be the same size"
        return sub_arr
    def __truediv__(self,B):
        '''
        This method overloads the division operator to perform element-wise division on an array. It supports division by scalars (integers or floats) as well as arrays of the same size.

        Parameters
        ----------
        B : int, float, array, nested list
        
        Returns
        -------
        div_arr : array
        '''
        #make a copy of the self array to get an array of the same shape
        r, c = self.shape
        div_arr = [[0] * c for i in range(r)] 
        #make an if statement for when dividing an integer or a float to an array 
        if type(B) == int or type(B) == float:
            #if the number of rows greater than 1, it's a 2D array or column vector
            if r>1:
                # iterate through each element of the array 
                for i in range(r):
                    for j in range(c):
                        div_arr[i][j] = self.data[i][j] / B
            # for a 1D array 
            elif r == 1:
                div_arr = div_arr[0]
                #iterate through 1D array 
                for i in range(len(div_arr)):
                    div_arr[i] = self.data[i] / B
        elif type(B) == list:
            B_arr = array(B)
            if B_arr.shape == self.shape:
                # for a 2D array
                if r > 1:
                    for i in range(len(self.data)):
                        for j in range(len(self.data[i])):
                            div_arr[i][j] = self.data[i][j] / B_arr.data[i][j]
                # if the self array has one row, it's a 1D array 
                elif r == 1:
                    div_arr = div_arr[0]
                    for i in range(len(self.data)):
                        div_arr[i] = self.data[i] / B_arr.data[i]
            else:
                div_arr = "Error: Arrays must be the same size"
        #when dividing with an array
        elif type(B.data) == list:
            if B.shape == self.shape:
                #for a 2D array
                if r > 1:
                    for i in range(len(self.data)):
                        for j in range(len(self.data[i])):
                            div_arr[i][j] = self.data[i][j] / B.data[i][j]
                #if the self array has one row, it's a 1D array 
                elif r == 1:
                    div_arr = div_arr[0]
                    for i in range(len(self.data)):
                        div_arr[i] = self.data[i] / B.data[i]
            else:
                div_arr = "Error: Arrays must be the same size"
        return div_arr    
    def __neg__(self):
        '''
        This method returns the negated object by overloading the neg operator (-obj).

        Returns
        -------
        neg_arr : array        

        '''
        #make a copy of the self array to get an array of the same shape
        r, c = self.shape
        neg_arr = [[0] * c for i in range(r)] 
        #if the number of rows greater than 1, it's a 2D array or column vector
        if r > 1:
            # iterate through each element of the array 
            for i in range(r):
                for j in range(c):
                    neg_arr[i][j] = self.data[i][j] * -1
        #for a 1D array
        elif r == 1:
            neg_arr = neg_arr[0]
            #iterate through 1D array 
            for i in range(len(neg_arr)):
                neg_arr[i] = self.data[i] * -1    
        return neg_arr   
    def __pow__(self,B):
        '''
        This method overloads the power operator to perform element-wise operation on an array. It supports raising the elements of the array to a power of a scalar (integer or float)
        Parameters
        ----------
        B : int, float

        Returns
        -------
        pow_arr : array 

        '''
        #make a copy of the self array to get an array of the same shape
        r, c = self.shape
        pow_arr = [[0] * c for i in range(r)] 
        #make an if statement for when raising the power by an integer or a float to an array 
        if type(B) == int or type(B) == float:
            #if the number of rows greater than 1, it's a 2D array or column vector
            if r > 1:
                # iterate through each element of the array 
                for i in range(r):
                    for j in range(c):
                        pow_arr[i][j] = self.data[i][j] ** B
            # for a 1D array 
            elif r == 1:
                pow_arr = pow_arr[0]
                #iterate through 1D array 
                for i in range(len(pow_arr)):
                    pow_arr[i] = self.data[i] ** B        
        else:
            pow_arr = 'This is not an integer or float value!'
        return pow_arr    
    def __getitem__(self, B):
        '''
        This method returns the element at the specified position. 
        Parameters
        ----------
        B : tuple of length 2 (x,y), element x specifying row position and element y specifying column position, according to python notation (starting from 0)

        Returns
        -------
        item : integer or float 
        '''
        #unpacking the tuple to get positions of row and column for element to be extracted
        x, y = B
        # get the dimensions of the array in self.data
        r, c = self.shape
        # for a 2D array 
        if r > 1 and c > 1:
            item = self.data[x][y]
        # for a row vector
        elif r == 1:
            item = self.data[y]
        # for a column vector
        elif c == 1:
            item = self.data[x][0]
        # error message 
        else:
            item = 'Index out of range!'
        return item
    def dot(self,B):
        '''
        This method performs the matrix dot product between 2 arrays

        Parameters
        ----------
        self.data : An array of dimensions (m,n)
        B : An array of dimensions (n,k)

        Returns
        -------
        C : An array of dimensions (m,k) after dot product
        '''
        #unpack dimensions of self.data 
        m,n = self.shape
        #unpack dimensions of B
        if type(B)==list:
            B = array(B)
        x,y = B.shape
        #check if dot product can be carried out or not by looking at first array's columns is equal to second array's rows
        if n == x:
            # make an array filled with zeros which are the dimensions of the resultant dot product 
            C = [[0] * y for i in range(m)] 
            # to calculate the dot product            
            if m > 1 and x > 1: # for multiplying 2D arrays 
                for i in range(m):
                    for j in range(y):
                        total = 0 #stores the sum of operations
                        for k in range(n):
                            total += self.data[i][k] * B.data[k][j]
                        C[i][j] = total
            elif m == 1 and y == 1: # if the first array is a row vector and second vector is a column vector
                total = 0 #stores the sum of operations
                for i in range(n):                    
                    total += self.data[i] * B.data[i][0]
                C = [[total]] 
            elif n == 1 and x == 1: # if the first array is a column vector and second vector is a row vector
                for i in range(m):
                    for j in range(y):
                        total = 0 #stores the sum of operations
                        total += self.data[i][0] * B.data[j]
                        C[i][j] = total                
            elif m == 1: #if the first array is a row vector 
                for i in range(m):
                    for j in range(y):
                        total = 0 #stores the sum of operations
                        for k in range(n):
                            total += self.data[k] * B.data[k][j]
                        C[i][j] = total    
            elif x == 1: #if the second array is a column vector
                for i in range(m):
                    for j in range(y):
                        total = 0 #stores the sum of operations
                        for k in range(n):
                            total += self.data[i][k] * B.data[k]
                        C[i][j] = total                        
            return C            
        else:
            return ('Dot product not possible!')
    def mean(self, mean_type=2):
        '''
        Parameters
        ----------
        mean_type : int - 0,1,2
            DESCRIPTION. The default is 2 - the mean of all elements in the array. 0 gives the mean of all the elements along the row and 1 returns the mean of all the elements along the column. 
    
        Returns
        -------
        mean : float value of elements in array 
        '''
        # calling method sum to return the sum of selected or all elements(default)       
        sum_elem = self.sum(mean_type)
        m,n = self.shape
        #if mean of all elements needs to be calculated
        if mean_type == 2:
            mean = sum_elem / self.size
        #if mean of all elements along the column needs to be taken
        elif mean_type == 1:
            sum_elem = array(sum_elem)
            mean = sum_elem.__truediv__(m) 
        elif mean_type == 0:
            sum_elem = array(sum_elem)           
            mean = sum_elem.__truediv__(n)
        return mean 
    def var(self):
        '''This function returns covariance of the given matrix. It assumes that the different features of the data (e.g. different time points, generally different components of a single experiment) will be aligned along columns and that different experiments will be aligned along rows. So each row represents a different experiment, consisting of columns corresponding to the different features of a single experiment. Given a data array X, covariance matrix C of X is defined in the following way: C =1/n(XTc·Xc),where Xc = X − X¯ and X¯ is the average of X taken over different experiments, and has the appropriate shape.'''
        # r is the number of rows, c is the number of column
        r,c = self.shape
        # assigning variable n that stores the number of rows
        n = r
        # calling the mean function to generate mean along the y axis
        x_bar = [self.mean(1)]
        # multiplying the result of previous step with n
        x_new_bar = x_bar * n
        # making an array object of the resulting matrix
        X_bar = array(x_new_bar)
        # subtracting X_bar from the original array
        x_c = self.__sub__(X_bar)
        # making an array object of the resulting matrix
        X_c = array(x_c)
        # calling the transpose function
        x_c_T = X_c.transpose()
        # making an array object of the resulting matrix
        X_c_T = array(x_c_T)
        # calling the dot function to generate the dot product of X_c and X_c_T
        c_n = X_c_T.dot(X_c)
        # making an array object of the resulting matrix
        C_n = array(c_n)
        # calling the truedivision function 
        C = C_n.__truediv__(n)
        return C