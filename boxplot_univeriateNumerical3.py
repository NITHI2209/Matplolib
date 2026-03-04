import matplotlib.pyplot as plt
import pandas as pd
data = {
    "salary" : [0,50000,70000,50000,60000,45000,80000,45000,30000]
}
df = pd.DataFrame(data)
plt.boxplot(df["salary"])
plt.show()
#Refer figure 4 ,5 