import numpy as np
import pandas as pd

x_mu, x_sigma = 250, 100
y_mu, y_sigma = 200, 80

xleaves = np.random.normal(x_mu, x_sigma, 300)
yleaves = np.random.normal(y_mu, y_sigma, 300)
df = pd.DataFrame({"xleaves" : xleaves, "yleaves" : yleaves})
df.to_csv("leaves.csv", index=False)

# np.savetxt('xleaves.csv', xleaves, delimiter=',')
# np.savetxt('yleaves.csv', yleaves, delimiter=',')