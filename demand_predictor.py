import pandas as pd
from sklearn.linear_model import LinearRegression

class DemandPredictor:
    def __init__(self):
        self.model = LinearRegression()
        self.trained = False

    def train(self, X, y):
        self.model.fit(X, y)
        self.trained = True

    def predict(self, X):
        if not self.trained:
            # Fallback: just return sum of crowd
            return X.sum(axis=1)
        return self.model.predict(X)

if __name__ == "__main__":
    # Example usage
    df = pd.DataFrame({'Ghatkopar':[200,220],'Andheri':[180,210],'Dadar':[150,170]})
    y = [600, 650]
    dp = DemandPredictor()
    dp.train(df, y)
    print(dp.predict(df))
