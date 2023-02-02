from fruit_analyzer import FruitAnalyzer
from visualize_fruit import VisualizeFruit

class FruitMediator:

    def __init__(self):
        self.fruit_analysis = FruitAnalyzer()

        self.fruit_viz = VisualizeFruit(self.fruit_analysis) 
        

    def get_graph_of_choice(self,graph_str):
        if graph_str == 'Distribution Chart':
            return self.fruit_viz.get_distribution_chart()
        elif graph_str == 'Hot Take':
            return self.fruit_viz.get_hot_take_bar()
        else:
            raise ValueError(f'Graph String: {graph_str} not recognized.  Check options in fruit_dash.')
        