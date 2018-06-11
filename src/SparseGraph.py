'''
Created on Jun 11, 2018

@author: Balakrishna Akuleti
'''
import numpy as np
import pandas as pd
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import csgraph_from_dense

g_dense = np.array( [   [0,2,1],
                        [2,0,0],
                        [1,0,0] ]  )
g_masked = np.ma.masked_values(g_dense, 0)

g_sparsed = csr_matrix(g_dense)

print( g_sparsed.data)

g2_data = np.array([
   [np.inf, 2, 0 ],
   [2, np.inf, np.inf],
   [0, np.inf, np.inf]
])

g2_sparse = csgraph_from_dense(g2_data, null_value=np.inf)
print (g2_sparse.data)

