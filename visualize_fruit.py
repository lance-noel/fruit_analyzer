import plotly.graph_objects as go
from plotly.subplots import make_subplots

class VisualizeFruit:

    def __init__(self,fruit_class):
        self.fruit_class = fruit_class
        self.cse_approved_colors={'grass': '#92c956', 
                                'mint': '#59b994', 
                                'jade': '#1F9D7F', 
                                'aqua': '#0796E6', 
                                'cobalt': '#3064BE', 
                                'grape': '#6D57C7', 
                                'violet': '#894CAF', 
                                'ruby': '#a3362b', 
                                'tangerine': '#f26522', 
                                'pumpkin': '#ef941b', 
                                'gold': '#ffc20e', 
                                'lemon': '#d4d835', 
                                'salmon': '#e97959', 
                                'raspberry': '#cc2e76', 
                                'charcoal': '#3C444C', 
                                'gray': '#9BA7B1',
                                'silver': '#C4CDD5',
                                'off_white':'#F5F6F6', 
                                'grass_alpha':'rgba(146,201,86,0.5)', 
                                'jade_alpha': 'rgba(31,157,127,0.5)',
                                'ruby_alpha':'rgba(163,54,43,0.5)',
                                'tangerine_alpha': 'rgba(242,101,34,0.5)',
                                'gold_alpha': 'rgba(255,194,14,0.5)',
                                'raspberry_alpha':'rgba(204,46,118,0.5)', 
                                'charcoal_alpha':'rgba(60,68,76,0.7)'}
        self.default_color_order=[self.cse_approved_colors['cobalt'], self.cse_approved_colors['raspberry'],self.cse_approved_colors['jade'],
                                self.cse_approved_colors['grape'],self.cse_approved_colors['ruby'],self.cse_approved_colors['grass'],
                                self.cse_approved_colors['violet'],self.cse_approved_colors['tangerine']]        

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
            line=dict(color=self.cse_approved_colors['grape'],width=6),
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
            line=dict(color=self.cse_approved_colors['tangerine'],width=4)
        ),secondary_y=True)


        fig.update_xaxes(title='Fruit')

        fig.update_yaxes(title='Average Rating',secondary_y=False)

        fig.update_yaxes(title='Standard Deviation',secondary_y=True)

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