from dash import Dash, html, dash_table, dcc, Input, Output, callback
import pandas as pd
import plotly.express as px
from get_data import table_scrape

table_scrape()

df = pd.read_csv('output_data.csv')

app = Dash(__name__)

app.layout = html.Div([
    html.Div(children="Accounting reports for 2012-2020"),
    html.Hr(),
    dcc.RadioItems(options=['Fixed assets', 'Accounts receivable', 'Accounts payable'],
                   value='Fixed assets', id='controls-and-radio-item'),
    dash_table.DataTable(data=df.to_dict('records'), page_size=6),
    dcc.Graph(figure={}, id='graph-item')
])


@callback(
    Output(component_id='graph-item', component_property='figure'),
    Input(component_id="controls-and-radio-item", component_property='value')
)
def graph_update(col_chosen):
    if col_chosen == 'Fixed assets':
        figure = {
            "data": [
                {
                    "x": df.columns.tolist()[1:],
                    "y": df.loc[0, :].tolist()[1:],
                    "name": "Fixed_assets",
                    "type": "scatter",
                }
            ],
            "layout": {
                "title": dict(text="Fixed assets per years")
            }
        }
        return figure
    elif col_chosen == "Accounts receivable":
        figure = {
            "data": [
                {
                    "x": df.columns.tolist()[1:],
                    "y": df.loc[4, :].tolist()[1:],
                    "name": "Accounts receivable",
                    "type": "scatter",
                }
            ],
            "layout": {
                "title": dict(text="Accounts receivable per years")
            }
        }
        return figure
    elif col_chosen == "Accounts payable":
        figure = {
            "data": [
                {
                    "x": df.columns.tolist()[1:],
                    "y": df.loc[12, :].tolist()[1:],
                    "name": "Accounts payable",
                    "type": "scatter",
                }
            ],
            "layout": {
                "title": dict(text="Accounts payable per years")
            }
        }
        return figure


if __name__ == '__main__':
    app.run_server(debug=True)
