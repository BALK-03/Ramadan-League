## Overview

In this problem, you will debug an implementation of a Univariate Linear Regression model. The provided code contains bugs. Your task is to find and fix the bugs to create a properly functioning model.

## Background

Linear Regression is one of the foundational algorithms in machine learning, used to model the relationship between a dependent variable (y) and one or more independent variables (X) by fitting a linear equation to the observed data. In Univariate Linear Regression, we have just one independent variable.

The model uses the following equation for prediction:
```
y = θ₀ + θ₁x
```
Where:
- θ₀ is the intercept (bias)
- θ₁ is the slope (weight)

## The Challenge

The provided `UnivariateLinearRegression` class contains implementations of:
- Model initialization
- Hypothesis function
- Cost computation
- Gradient descent optimization
- Model fitting and prediction
 
Your tasks are to:
1. Identify and fix the bugs
2. Demonstrate that your fixes work by running the model on the generated sample, Expected output:
    - Trained parameters: θ₀ = 3.2396, θ₁ = 1.9373
    - Mean Absolute Error (MAE): 1.4165
