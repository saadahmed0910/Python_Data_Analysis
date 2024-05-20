#!/usr/bin/env python
# coding: utf-8

# In[47]:


import numpy as np

def calculate(the_list):
    if len(the_list) <9:
        raise ValueError(f"List must contain nine numbers.")
    else:
    
        array = np.array(the_list)
        matrix = array.reshape(3,3)

        mean_a1 = []
        mean_a2 = []
        mean_flat = np.mean(matrix.flatten())
        var_a1 = []
        var_a2 = []
        var_flat = np.var(matrix.flatten())
        std_a1 = []
        std_a2 = []
        std_flat = np.std(matrix.flatten())
        max_a1 = []
        max_a2 = []
        max_flat = max(matrix.flatten())
        min_a1 = [] 
        min_a2 = [] 
        min_flat = min(matrix.flatten())
        sum_a1 = []
        sum_a2 = []
        sum_flat = sum(matrix.flatten())




        for i in range(1):


            for k in range (len(matrix)):
                #print(matrix.transpose()[k])

                mean_a2.append(np.mean(matrix[k]))
                var_a2.append(np.var(matrix[k]))
                std_a2.append(np.std(matrix[k]))
                max_a2.append(max(matrix[k]))
                min_a2.append(min(matrix[k]))
                sum_a2.append(sum(matrix[k]))

                mean_a1.append(np.mean(matrix.transpose()[k]))
                var_a1.append(np.var(matrix.transpose()[k]))
                std_a1.append(np.std(matrix.transpose()[k]))
                max_a1.append(max(matrix.transpose()[k]))
                min_a1.append(min(matrix.transpose()[k]))
                sum_a1.append(sum(matrix.transpose()[k]))

        total_mean = [mean_a1, mean_a2, mean_flat]
        total_var = [var_a1, var_a2, var_flat]
        total_std = [std_a1, std_a2, std_flat]
        total_max = [max_a1, max_a2, max_flat]
        total_min = [min_a1, min_a2, min_flat]
        total_sum = [sum_a1, sum_a2, sum_flat]

        calculations = {
            "mean": total_mean,
            "variance": total_var,
            "standard deviation": total_std,
            "max": total_max,
            "min": total_min,
            "sum": total_sum
        }
    
    
                
        
    return calculations

calculate([0,1,2,3,4,5,6,8])


# In[ ]:




