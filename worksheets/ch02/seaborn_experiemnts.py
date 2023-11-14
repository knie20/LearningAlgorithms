import seaborn as sns
import matplotlib.pyplot as plt

# Load a built-in Seaborn dataset
data = sns.load_dataset('iris')

# Create a simple plot - for example, a scatter plot
sns.scatterplot(x='sepal_length', y='sepal_width', data=data)

# Show the plot
plt.show()