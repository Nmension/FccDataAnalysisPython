import numpy as np

def calculate(list):
    if len(list) == 9:
        #np 3x3 matrix obtained from the lsit arg of the function
        matrix = np.reshape(np.array(list), (3,3))
        final_result = {}
        col = 0
        row = 0

        #lists to store the values of each of the rows in the final result dict
        mean_l = []
        var_l = []
        std_l = []
        max_l = []
        min_l = []
        sum_l = []

        #lists for the first axis: axis1, first element for each row, according to their operations
        axis1_m = []
        axis1_v = []
        axis1_s = []
        axis1_max = []
        axis1_min = []
        axis1_sum = []

        #lists for the second axis: axis2, second element for each row, according to their operations
        axis2_m = []
        axis2_v = []
        axis2_s = []
        axis2_max = []
        axis2_min = []
        axis2_sum = []

        if len(final_result) == 0:
            for _ in matrix:
                #for all rows of the matrix (start:last_index+1), start with the first column indexed 0, until the third indexed 2, and store the result of their respective operations in different variables
                #then convert the result to the desired python format before appending it to their respective list for the first axis
                if col < 3:
                    #for one col:
                    #calc mean for col
                    col_mean = np.mean(matrix[:3,col])
                    #calc var for col of the matrix
                    col_var = np.var(matrix[:3,col])
                    #calc std for col
                    col_std = np.std(matrix[:3,col])
                    #find max for col
                    col_max = np.max(matrix[:3,col])
                    #find min for col
                    col_min = np.min(matrix[:3,col])
                    #calc sum for col
                    col_sum = np.sum(matrix[:3,col])

                    #for the current col, append respective result to respective axis1 list, and do this for all cols (until col == 2) to get the axis1 list
                    axis1_m.append(float(col_mean))
                    axis1_v.append(float(col_var))
                    axis1_s.append(float(col_std))
                    axis1_max.append(int(col_max))
                    axis1_min.append(int(col_min))
                    axis1_sum.append(int(col_sum))

                    #pass to the next col
                    col += 1

                    #for each, when the list storing the elements for axis1 == 3
                    #append the respective resulting list to another one 
                    #which each will later represent the first element of different rows in the final object dict
                    if len(axis1_m) == 3:
                        mean_l.append(axis1_m)
                    if len(axis1_v) == 3:
                        var_l.append(axis1_v)
                    if len(axis1_s) == 3:
                        std_l.append(axis1_s)
                    if len(axis1_max) == 3:
                        max_l.append(axis1_max)
                    if len(axis1_min) == 3:
                        min_l.append(axis1_min) 
                    if len(axis1_sum) == 3:
                        sum_l.append(axis1_sum)

                #for each row of the matrix, calc their mean|var|std|max|min|sum then convert each result to the python desired format 
                #append each result to its respective list for the second axis, axis2
                #when the number of elements in each list for axis2 also reaches 3, append their resulting list as the second element for each row in the final object
                if row < 3:
                    #for one row:
                    #calc mean for row
                    row_mean = np.mean(matrix[row])
                    #cal var for row
                    row_var = np.var(matrix[row])
                    #calc std for row
                    row_std = np.std(matrix[row])
                    #find max of row
                    row_max = np.max(matrix[row])
                    #find min of row
                    row_min = np.min(matrix[row])
                    #cal sum for row
                    row_sum = np.sum(matrix[row])

                    axis2_m.append(float(row_mean))
                    axis2_v.append(float(row_var))
                    axis2_s.append(float(row_std))
                    axis2_max.append(int(row_max))
                    axis2_min.append(int(row_min))
                    axis2_sum.append(int(row_sum))
                    #same logic as before but by row
                    if len(axis2_m) == 3:
                        mean_l.append(axis2_m)
                    if len(axis2_v) == 3:
                        var_l.append(axis2_v)
                    if len(axis2_s) == 3:
                        std_l.append(axis2_s)
                    if len(axis2_max) == 3:
                        max_l.append(axis2_max)
                    if len(axis2_min) == 3:
                        min_l.append(axis2_min)
                    if len(axis2_sum) == 3:
                        sum_l.append(axis2_sum)
                    
                    #pass to the next row
                    row += 1

                #for each, mean_l|var_l|std_l|max_l|min_l, since the list which represents the rows in the final object has 2 elements at this point, 
                #append to each respective list, a third element's result depending on their respective operations but this time using all elements of the matrix
                if len(mean_l) == 2:
                    mean_l.append(float(np.mean(matrix)))
                if len(var_l) == 2:
                    var_l.append(float(np.var(matrix)))
                if len(std_l) == 2:
                    std_l.append(float(np.std(matrix)))
                if len(max_l) == 2:
                    max_l.append(int(np.max(matrix)))
                if len(min_l) == 2:
                    min_l.append(int(np.min(matrix)))
                if len(sum_l) == 2:
                    sum_l.append(int(np.sum(matrix)))
            
            #add each row's list of the final dict obj (final_results) as values
            final_result.update({'mean': mean_l, 'variance': var_l, 'standard deviation': std_l, 'max': max_l, 'min': min_l, 'sum': sum_l})


        #when the final_result dict/object has 6 elements, return the dict, 
        #the commented code before the return statement bellow is to get asked format on fcc but looking at the unit tests, it just asks for the dict as it is ?
        if len(final_result) == 6:
            #str_result = "{\n"
            #for key, value in final_result.items():
            #    str_result += f"  '{key}': {value},\n"
            return final_result

    #Value error raised when list hasn't 9 nums
    else:
        raise ValueError("List must contain nine numbers.")