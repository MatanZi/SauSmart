

class FeatureCalculator:

    def __init__(self, df):
        self.df = df

    def max_change(self):
        return self.df['diff'].max()

    def min_change(self):
        return self.df['diff'].min()

    def std_change(self):
        return self.df['diff'].std()

    def var_change(self):
        return self.df['diff'].var()

    def mean_change(self):
        return self.df['diff'].mean()

    def sum_change(self):
        return self.df['diff'].sum()

    def size_change(self):
        return len(self.df['diff'])
