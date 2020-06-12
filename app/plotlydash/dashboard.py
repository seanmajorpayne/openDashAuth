import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
from app import routes
from app.models import User

def create_dashboard(server):
    """Create a Plotly Dash dashboard embedded within Flask"""
    dash_app = dash.Dash(server=server,
                        routes_pathname_prefix='/dashapp/',
                        external_stylesheets=[dbc.themes.CERULEAN]
    )
		

    dash_app.layout = html.Div(children=[
        html.Div([
            html.Div([
                html.H1(id="my-header", className="text-center"),
            ], className="col-md-12")
        ], className="row"),			
        html.A('Login', id="login-link", href="/login"),
        html.Div(id="my-div", className="text-center"),
        html.Button(id='submit-button-state', n_clicks=1, children='Submit',
        style={'display': 'none'}),
    ])
	
	
    @dash_app.callback(
        [Output(component_id='my-header', component_property='children'),
        Output(component_id='my-div', component_property='children'),
        Output(component_id='login-link', component_property='style')],
        [Input(component_id='submit-button-state', component_property='n_clicks')]
    )
	
    def get_user_name(n_clicks):
        """
        The dashboard only loads if a user is authenticated
        """
        if routes.get_user().is_authenticated:
            welcome_msg = "Welcome back, " + routes.get_user().username
            user_data = load_data()
            link_style = {'display':'none'}
            return welcome_msg, user_data, link_style
        return "Your Princess is in another castle", ''


    def load_data():
        """
        The user's data is pulled from a database. As the user has already been
        authenticated, the 'current_user' from 'flask_login' is used within a database
        query, ensuring that the correct user's data is loaded. This is the key to
        having multiple user authentication with dedicated views for each user.
        """
        x = []
        y = []
        u = routes.get_user()
        data = u.data_for_user.all()
        for d in data:
            x_data = [d.x1, d.x2, d.x3]
            y_data = [d.y1, d.y2, d.y3]
        return html.Div([
                    html.Div([
                        dcc.Graph(
                            id='client-data',
                            figure={
                                'data': [
                                    {'x': x_data , 'y': y_data, 
                                    'type': 'scatter', 'name': 'Data'}
                                ],
                                'layout': {
                                    'title': 'Customer Data',
                                    'plot_bgcolor': '#252e3f',
                                    'paper_bgcolor': '#252e3f',
                                    'font': dict(color='#FFFFFF'),
                                    'xaxis': dict(title='x axis',
                                                    color='#98FB98',
                                    ),
                                    'yaxis': dict(title='y axis',
                                                    color='#98FB98'
                                    ),
                                    'line': dict(color='#98FB98')
                                },
                            }
                        )
                    ], className="col-md-8")
                ], className="row justify-content-center")
	
	
	
    return dash_app.server