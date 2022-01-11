# %% [markdown]
# # Jupyternootbook in VScode
# This is much better than other jupyternotebook 

# %%
print('python ka chilla')

# %%
aammar= "The tutor name is aammar"
aammar

# %%
import numpy as np
x = np.array([1,2,5,6,7,9,5])
x


# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
 
phool = pd.read_csv("iris.csv")

# %%
import pandas as pd
import matplotlib.pyplot as plt
iris = pd.read_csv("Iris.csv")
 
plt.plot(iris.Id, iris["SepalLengthCm"], "r--")
plt.show




# %%
import seaborn as sns
import matplotlib.pyplot as plt
# set a grey background (use sns.set_theme() if seaborn version 0.11.0 or above) 
sns.set(style="darkgrid")
df = sns.load_dataset('iris')

sns.boxplot(x=df["species"], y=df["sepal_length"], palette="Blues")
plt.show()

# %%
pip install seaborn
pip install pdf


# %%



