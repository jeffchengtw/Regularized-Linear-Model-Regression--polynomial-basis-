import numpy as np

'''
formula
1 / det(A) * adjA
'''
def minormatrix(m, row, col):
    return [i[:col]+i[col+1:] for i in (m[:row]+m[row+1:])]

def compute_det(m):
    m_length = len(m)
    if m_length == 2:
        dmt = (m[0][0]*m[1][1]) - (m[0][1]*m[1][0])
    else:
        dmt = 0
        for col in range(m_length):
            minor = minormatrix(m,0,col)
            dmt += ((-1)**col)*m[0][col] * compute_det(minor)
    return dmt

def inverse(m):
    if isinstance(m, np.ndarray):
        m = m.tolist()
    dmt = compute_det(m)
    m_length = len(m)
    if m_length == 2:
        molecular = np.array([[m[1][1], -m[0][1]],
                            [-m[1][0], m[0][0]]])
        mInverse = molecular / dmt
    else:
        molecular = []
        for row in range(m_length):
            molecular_row = []
            for col in range(m_length):
                minor = minormatrix(m,row,col)
                molecular_row.append(((-1)**(row+col)) * compute_det(minor))
            molecular.append(molecular_row)
        mInverse = (np.array(molecular).T) / dmt
    return mInverse