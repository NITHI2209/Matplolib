import matplotlib.pyplot as plt
import pandas as pd
data = {
    "salary" : [50000,70000,55000,60000,45000,80000]
}
df = pd.DataFrame(data)
plt.plot(df["salary"])
plt.show()
#Refer figure 2