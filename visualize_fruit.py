import plotly.graph_objects as go
from plotly.subplots import make_subplots

class VisualizeFruit:

    def __init__(self,fruit_class):
        self.fruit_class = fruit_class
        

    def get_distribution_chart(self):
        main_fruit_df = self.fruit_class.main_fruit_df.copy()
        main_fruit_df = main_fruit_df.sort_values(by=['Average'],ascending = False)

        people = [k for k in main_fruit_df.keys() if k not in ['Average','STD']]

        fig = make_subplots(specs=[[{"secondary_y": True}]])
        fig.add_trace(go.Scatter(
            mode='lines+markers',
            x=main_fruit_df.index,
            y=main_fruit_df['Average'],
            name='Average',
            line=dict(color='firebrick',width=6),
            # error_y=dict(
            #     type='data',
            #     symmetric=True,
            #     array=main_fruit_df['STD'],  
            # )


        ),secondary_y=False
        )
        fig.add_trace(go.Scatter(
            mode='lines+markers',
            x=main_fruit_df.index,
            y=main_fruit_df['STD'],
            name='Standard Deviation',
            line=dict(color='aqua',width=5)
        ),secondary_y=True)


        fig.update_xaxes(title='Fruit')

        fig.update_yaxes(title='Average Rating')

        return fig

    def get_hot_take_bar(self):
        hot_take_df = self.fruit_class.fruit_variance_df.loc['Average'].T

        hot_take_df = hot_take_df.sort_values(ascending=False)

        hot_take_fig = go.Figure()

        hot_take_fig.add_trace(go.Bar(
            x=hot_take_df.index,
            y=hot_take_df.values
        ))

        hot_take_fig.update_yaxes(title='Average Variance')

        hot_take_fig.update_layout(title='People with the Highest Fruit Variance')

        return hot_take_fig