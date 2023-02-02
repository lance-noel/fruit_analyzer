from dash import html, dcc, Dash
from dash.dependencies import Input, Output, State
from fruit_mediator import FruitMediator

fruit_mediator_obj = FruitMediator()

app = Dash(__name__)

app.layout = html.Div([
    html.Div(
        id = 'inputs_div',
        children=[
            html.B('Welcome to the Interactive Fruit Survey'),
            html.Br(),
            html.Div([
                html.I('Please select graph type:'),
                dcc.Dropdown(
                    id='graph_str',
                    options = [{'label':i,'value':i} for i in ['Distribution Chart','Hot Take']],
                    style = {'height':'30px','width':'150px'}
                )
            ],
            style={'display':'inline-flex'}),
        ],
        style={'display':'block'}),
        html.Div(
            id='graph_div',
            children=[
                dcc.Graph(
                    id = 'main_graph',
                    style = {'width':'98vw','height':'70vh'},
                    config={'displaylogo': False, 'modeBarButtonsToRemove': ['toImage']}
                )
            ],
            style={'display':'block'}
        )        
])

@app.callback(
    Output('main_graph','figure'),
    Input('graph_str','value')
)
def update_figure(graph_str):
    return_fig = fruit_mediator_obj.get_graph_of_choice(graph_str)
    return return_fig

if __name__ == '__main__':
    app.run_server(debug=False, port=7777)