import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('Dataset.csv')

price_range = data['Price range']
plt.hist(price_range)
plt.show()

price_count = price_range.value_counts()
total_hotel = price_range.size
print(total_hotel)
per = (price_count/total_hotel) * 100
print('Percentage of restaurants in each price range category: ')
print(per)
