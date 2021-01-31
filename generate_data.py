import numpy as np
import pandas as pd
from scipy.stats import skewnorm
import random

# x_mu, x_sigma = 250, 100
num = 1750
y_mu, y_sigma = 200, 70
# xleaves = np.random.normal(x_mu, x_sigma, 300) 
# yleaves = np.random.normal(y_mu, y_sigma, 300)

xleaves = np.random.default_rng().uniform(50,450,num) # even distribution
# yleaves = skewnorm(1, 0, 300).rvs(size=num) # high (right) skewed ditribution
yleaves = np.random.normal(y_mu, y_sigma, num*2) # normal distribution
yleaves = np.delete(yleaves, np.where(yleaves >= 300)) # convert to skewed distribution
dif = np.absolute(len(xleaves) - len(yleaves))
if len(xleaves) > len(yleaves):
    xleaves = xleaves[:-dif]
elif len(yleaves) > len(xleaves):
    yleaves = yleaves[:-dif]

color = random.choices(
                population=[0,1,2,3,4],
                weights=[0.05,0.3,0.26,0.22,0.17],
                k=len(yleaves))

print(max(yleaves))
print(min(yleaves))

print(max(xleaves))
print(min(xleaves))


# save as csv
df = pd.DataFrame({"xleaves" : xleaves, "yleaves" : yleaves, "color" : color})
df.to_csv("leaves.csv", index=False)
