# Assignment 6: Basics of Machine Learning

## Problem Statement / Aim
To understand the basics of Machine Learning by implementing a Simple Linear Regression model from scratch to predict target values based on a single input feature.

## Theory & Concept
Machine Learning is a subset of AI that allows systems to learn from data. Simple Linear Regression is a supervised learning algorithm that models the relationship between a single independent variable (X) and a dependent variable (Y) by fitting a linear equation to observed data. 
The equation of the regression line is `Y = mX + c`, where:
- `m` is the slope of the line, representing the change in Y for a one-unit change in X.
- `c` is the y-intercept, representing the value of Y when X is 0.
The goal is to calculate the optimal `m` and `c` that minimize the error between the predicted and actual Y values, often using the Ordinary Least Squares (OLS) method.

## Fully Solved Code
```python
def mean(values):
    return sum(values) / float(len(values))

def calculate_slope_and_intercept(X, Y):
    x_mean = mean(X)
    y_mean = mean(Y)
    
    numerator = 0
    denominator = 0
    
    # Calculate the slope (m) and intercept (c) using Ordinary Least Squares
    for i in range(len(X)):
        numerator += (X[i] - x_mean) * (Y[i] - y_mean)
        denominator += (X[i] - x_mean) ** 2
        
    m = numerator / denominator
    c = y_mean - (m * x_mean)
    
    return m, c

def predict(X, m, c):
    predictions = []
    for x in X:
        y_pred = m * x + c
        predictions.append(y_pred)
    return predictions

if __name__ == "__main__":
    # Sample Dataset: Hours Studied (X) vs. Exam Score (Y)
    X_train = [1, 2, 3, 4, 5]
    Y_train = [2, 4, 5, 4, 5]
    
    print(f"Training Data (X): {X_train}")
    print(f"Training Data (Y): {Y_train}")
    
    m, c = calculate_slope_and_intercept(X_train, Y_train)
    
    print(f"\nCalculated Slope (m): {m:.2f}")
    print(f"Calculated Intercept (c): {c:.2f}")
    print(f"Regression Line Equation: Y = {m:.2f} * X + {c:.2f}")
    
    # Testing the model with a new value
    X_test = [6]
    predictions = predict(X_test, m, c)
    print(f"\nPrediction for {X_test[0]} hours of study: {predictions[0]:.2f}")
```

## Expected Output
```text
Training Data (X): [1, 2, 3, 4, 5]
Training Data (Y): [2, 4, 5, 4, 5]

Calculated Slope (m): 0.60
Calculated Intercept (c): 2.20
Regression Line Equation: Y = 0.60 * X + 2.20

Prediction for 6 hours of study: 5.80
```

[[CS-321-Viva-6|View Viva Questions]]
