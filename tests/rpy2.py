import rpy2
import rpy2.robjects as robjects
from rpy2.robjects.packages import importr

tmvtnorm = importr('tmvtnorm')


# Creating and using R functions 
print('----------------')
print('---- TEST 1 ----')
print('----------------')

robjects.r('''
        # create a function `f`
        f <- function(r, verbose=FALSE) {
            if (verbose) {
                cat("I am calling f().\n")
            }
            2 * pi * r
        }
        # call the function `f` with argument value 3
        f(3)
        ''')

r_f = robjects.r['f']
res = r_f(3)

print(res)



# Evaluating R code
print('----------------')
print('---- TEST 2 ----')
print('----------------')

print(robjects.r('''
        #library(tmvtnorm)
        mu <- c(0.5, 0.5)
        sigma <- matrix(c(1, 1.2, 1.2, 2), 2, 2)
        a <- c(-1, -Inf)
        b <- c(0.5, 1)
        moments <- mtmvnorm(mean=mu, sigma=sigma, lower=a, upper=b)
        moments
        '''))


# Same as TEST 2 using 'pythonic' commands
print('----------------')
print('---- TEST 3 ----')
print('----------------')

rmtmvnorm = robjects.r['mtmvnorm']

mu = robjects.FloatVector([0.5, 0.5])
sigma = robjects.r['matrix'](robjects.FloatVector([1, 1.2, 1.2, 2]), 2, 2)
a = robjects.FloatVector([-1, '-Inf'])
b = robjects.FloatVector([0.5, 1])
moments = rmtmvnorm(mean=mu, sigma=sigma, lower=a, upper=b)

print(moments)
