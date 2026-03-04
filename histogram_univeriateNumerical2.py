import matplotlib.pyplot as plt
import pandas as pd
data = {
    "salary" : [50000,70000,50000,60000,45000,80000,45000,30000]
}
df = pd.DataFrame(data)
plt.hist(df["salary"],bins=5,color="green")
plt.show()
# refer figure 3