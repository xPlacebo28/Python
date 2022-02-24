# DATE: 2/24/2022
# Source: www.towardsdatascience.com/explain-linear-regression-with-manual-calculation-1622affdce6b
# Author: placeboXego
#
# The purpose of this script is to review Linear Regression. 
# This method shows how the dependent variable (Y) relates to 
# an independent variable(s) (X) by a linear form of an equation.
# If there is only one independent variable this will be called a
# simple linear regression. If more than one inpdendent variable
# exists, it'll be a multiple linear regresssion.
#
#
#              n
#   Yi  = Bo + E (Bn xik) + ei
#             k=1
#          
#
# Yi  = dependent variable for the i-th observation
# xik = independent variable(s) for the i-th observation
# Bo  = the intercept
# Bn  = coefficient for xik
# ei  = error term for the i-th observation. 
#
# The mathematical definition of the coefficient is the partial
# deriviative of the dependent variable, with respect to the
# independent variable. In layman's terms, the coefficient tells you
# the change of the dependent variable when an independent variables
# by 1 while other independent variables keep constant. Apart from these 
# variables, there is a constant called the intercept and an error in the
# equation. The intercept will not be affected by the value of the 
# independent variable(s) while the error term captures the random error 
# that cannot be explained by the model. 
#
#
#

# Defining data
x = [1,3,5,8]
y = [5,9,18,25]

# To determine the values of Bo and B1, there are two estimation 
# methods, which are the least-squares and maximum likelihood estimation. 


# ------------------- LEAST SQUARES METHOD ------------------------------#
#b1 = Sxy/Sxx

              n                                        n      
# where Sxy = E (xi - xbar)(yi - ybar)     and   Sxx = E(xi - xbar)^2
             i=1                                      i=1          

# bo = ybar - b1xbar


# Solve for R^2 

# 1) SST is the total sum of squares
# 2) SSR is the regression sum of squares
# 3) SSE is the residual sum of squares

 #       n                                                                
 # SST = E (yi - ybar)^2                                                                      
 #      i=1                                                                 
                                                                       
#        n                                                                
#  SSR = E (yhat - ybar)^2                                                                      
#       i=1                                                                 
                                                                                                                                                                                                                  
#        n                                                                
#  SSE = E (yi - yhat)^2        OR   SSE = E(yi-yhat)^2 = E(yi - (bo+b1xi))^2                                                              
#       i=1                                                                 
                                                                                     
  
 # SST = SSR + SSE
 # ^ The total variation in the observed dependent variables is the sum of variation 
 # explained by the regression model and variation unexplained.
                                                                       
                                                                       
