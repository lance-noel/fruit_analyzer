import pandas as pd
import os
#The Fruit Form: https://tiermaker.com/create/fruit-but-it-has-a-lot-of-fruits-514755


class FruitAnalyzer:

    def __init__(self):

        self.cur_path = os.path.split(os.path.abspath(__file__))[0]

        self.main_fruit_df = pd.read_excel(os.path.join(self.cur_path,'raw_data','all_data.xlsx'))

        self.main_fruit_df = self.main_fruit_df.replace({-99:None}).set_index('Fruit')

        self.people = list(self.main_fruit_df.keys())

        self.main_fruit_df['Average'] = self.main_fruit_df.apply(lambda x: self.__get_average(x),axis=1)

        self.main_fruit_df['STD'] = self.main_fruit_df[self.people].std(axis=1)

        self.main_fruit_df['Count of S Ratings'] = (self.main_fruit_df[self.people]==5).sum(skipna=True,axis=1)

        self.main_fruit_df['Count of NaNs'] =pd.isna(self.main_fruit_df[self.people]).sum(axis=1)

        self.fruit_variance_df = self.__get_variance_df()

        self.top_fruit = list(self.main_fruit_df.sort_values(by=['Average'],ascending = False).index)

        self.most_divisive_fruit  = list(self.main_fruit_df.sort_values(by=['STD'],ascending = False).index)

        self.favorite_fruit = list(self.main_fruit_df.sort_values(by=['Count of S Ratings'],ascending = False).index)

        self.least_tried_fruit = list(self.main_fruit_df.sort_values(by=['Count of NaNs'], ascending = False).index)

    @staticmethod
    def __get_average(x):
        non_nan_count = 0
        total = 0
        for n in x:
            if n is not None:
                non_nan_count += 1
                total += n

        return total / non_nan_count


    def __get_variance_df(self):
        fruit_variance_df = pd.DataFrame(index=self.main_fruit_df.index,columns=self.people)

        for person in self.people:
            fruit_variance_df[person] = (self.main_fruit_df[person] - self.main_fruit_df['Average']).abs()
        fruit_variance_df.loc['Average'] = fruit_variance_df.mean()

        return fruit_variance_df



if __name__ == '__main__':
    get_all_plots = True
    f = FruitAnalyzer()
    print('top fruit')
    for n in range(10):
        print(n+1,f.top_fruit[n])
    print('favorite fruit')
    for n in range(10):
        print(n+1,f.favorite_fruit[n])
    print('most divisive')
    for n in range(10):
        print(n+1,f.most_divisive_fruit[n])
    print('least tried')
    for n in range(10):
        print(n+1,f.least_tried_fruit[n])

    if get_all_plots == True:
        from visualize_fruit import VisualizeFruit
        v = VisualizeFruit(f)
        from plotly.offline import plot
        plot(v.get_distribution_chart(),filename='outputs/distr_chart.html')
        plot(v.get_hot_take_bar(),filename='outputs/hot_take.html')