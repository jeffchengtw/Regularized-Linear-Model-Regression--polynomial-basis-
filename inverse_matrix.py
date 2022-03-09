import numpy as np
import math

def getMinorIndex(matrixLocal, x, y):
  minor = []
  for i in range(3):
    minorRow = []
    if i == x:
      continue
    for j in range(3):
      if j == y:
        continue
      minorRow.append(matrixLocal[i][j])
    minor.append(minorRow)
  return minor

def getDeterminant2By2(matrixLocal):
  determinant = matrixLocal[0][0] * matrixLocal[1][1] - matrixLocal[0][1] * matrixLocal[1][0]
  return determinant

def getDeterminant(matrixLocal):
  determinant = 0
  for x in range(3):
    t = getDeterminant2By2(getMinorIndex(matrixLocal, 0, x))
    e = matrixLocal[0][x]
    determinant += (t * e * math.pow(-1, x))
  return determinant

def getCofactorMatrix(matrixLocal):
  cofactorMatrix = []
  for i in range(3):
    row = []
    for j in range(3):
      e = matrixLocal[i][j]
      t = getDeterminant2By2(getMinorIndex(matrixLocal, i, j))
      row.append(t * math.pow(-1, i + j))
    cofactorMatrix.append(row)
  return cofactorMatrix

def transpose(matrixLocal):
  transposeMatrix = []
  for i in range(3):
    row = []
    for j in range(3):
      e = matrixLocal[j][i]
      row.append(e)
    transposeMatrix.append(row)
  return transposeMatrix

def divideMatrix(matrixLocal, divisor):
  ansMatrix = []
  for i in range(3):
    row = []
    for j in range(3):
      e = matrixLocal[i][j]/divisor
      row.append(e)
    ansMatrix.append(row)
  return ansMatrix

def inverse(matrix):
    cofactor = getCofactorMatrix(matrix)
    adjoint = transpose(cofactor)
    det = getDeterminant(matrix)
    ans = divideMatrix(adjoint, det)
    return ans
    print('------------------------------------my---------------------------------------')
    print(matrix)
    print(ans)
    print('------------------------------------my---------------------------------------')
