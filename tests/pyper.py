from pyper import *
# from patched_pyper import *
import pandas as pd
r=R(use_pandas=True)

# PypeR starts responding only after 5 R-commands. Bug?

r("library(tmvtnorm)")
r("mu <- c(0.5, 0.5)")
r("sigma <- matrix(c(1, 1.2, 1.2, 2), 2, 2)")
r("a <- c(-1, -Inf)")
r("b <- c(0.5, 1)")
r("moments <- mtmvnorm(mean=mu, sigma=sigma, lower=a, upper=b)")

print(r("moments"))
