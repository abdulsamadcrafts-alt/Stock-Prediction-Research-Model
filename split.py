import pandas as pd

train = pd.read_csv("Apple_Stock_Price_Train.csv")
test = pd.read_csv("Apple_Stock_Price_Test.csv")

print("Train rows:", len(train))
print("Test rows:", len(test))