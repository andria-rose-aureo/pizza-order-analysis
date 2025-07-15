import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = {
    'Day': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
    'Small':[10,12,8,11,14,18,13],
    'Medium':[8,9,10,7,11,15,12],
    'Large':[5,6,7,4,9,12,8]
}

df = pd.DataFrame(data)
df['total_orders'] = df[['Small', 'Medium', 'Large']].sum(axis=1)

max_orders = df.loc[df['total_orders'].idxmax()]
print(max_orders)

plt.figure(figsize=(10, 5))
plt.plot(df['Day'], df['Small'], label='Small', marker='o')
plt.plot(df['Day'], df['Medium'], label='Medium', marker='o')
plt.plot(df['Day'], df['Large'], label='Large', marker='o')


#pizza orders by size throughout the week
plt.title("Pizza Orders by Size Throughout the Week")
plt.xlabel("Day")
plt.ylabel("Number of Orders")
plt.legend()
plt.grid(True)
plt.show()

#total pizza orders per day
plt.figure(figsize=(8, 4))
sns.barplot(x='Day', y='total_orders', data=df, palette='pink')
plt.title("Total Pizza Orders Per Day")
plt.show()
