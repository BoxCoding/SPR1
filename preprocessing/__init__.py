import math


class data_processing:

    @staticmethod
    def filter_intvalue(df,col):
        df[col] = df[col].fillna(0)
        return df

    @staticmethod
    def filter_strvalue(df,col):
        df[col] = df[col].fillna('')
        return df

    @staticmethod
    def filter_floorno(x):
        if x == "Ground":
            x = 0
        elif x == "Upper Basement":
            x = -1
        elif x == "Lower Baserment":
            x = -2
        return x



    @staticmethod
    def counter_cosine_similarity(c1, c2):
        terms = set(c1).union(c2)
        dotprod = sum(c1.get(k, 0) * c2.get(k, 0) for k in terms)
        magA = math.sqrt(sum(c1.get(k, 0)**2 for k in terms))
        magB = math.sqrt(sum(c2.get(k, 0)**2 for k in terms))
        return dotprod / (magA * magB)