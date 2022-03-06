# Regularized Linear Model Regression (polynomial basis)
 
# Input Data
```
x_data = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
y_label = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]
```
# Output
## Case 1: n = 2, λ = 0
```
LSE:
Fitting line: 0.997470X^1 + 66.972701
Total error: 3232.939805

Newton's Method:
Fitting line: 0.997470X^1 + 66.972701
Total error: 3232.939805
```
![Case 1](https://github.com/jeffchengtw/Regularized-Linear-Model-Regression--polynomial-basis-/blob/main/n2l0.png)

## Case 2: n = 3, λ = 0
```
LSE:
Fitting line: 0.300185X^2 + -5.858585X^1 + 94.018124
Total error: 949.787726

Newton's Method:
Fitting line: 0.300185X^2 + -5.858585X^1 + 94.018124
Total error: 949.787726
```
![Case 2](https://github.com/jeffchengtw/Regularized-Linear-Model-Regression--polynomial-basis-/blob/main/n3l0.png)

## Case 3: n = 3, λ = 10000
```
LSE:
Fitting line: 0.270819X^2 + 0.227608X^1 + 0.055519
Total error: 39343.640970

Newton's Method:
Fitting line: 0.300185X^2 + -5.858585X^1 + 94.018124
Total error: 949.787726
```
![Case 2](https://github.com/jeffchengtw/Regularized-Linear-Model-Regression--polynomial-basis-/blob/main/n3l10000.png)
