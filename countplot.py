import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.pyplot as plt
import pandas as pd
data = {
    "salary": [12000,23000,33000,43000,43200,45000,45500,50000,55000,60000],
   "Dept" : ["HR","Finance","IT","HR","HR","IT","HR","Finance","Finance","HR"]

}
df = pd.DataFrame(data)
count = df["Dept"].value_counts()
plt.bar (count.index,count,color= ["grey","black","red"])
plt.show()
#Refer figure 7