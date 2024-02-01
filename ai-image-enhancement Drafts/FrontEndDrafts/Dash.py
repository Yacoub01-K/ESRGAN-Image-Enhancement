from dash import *
import plotly.express as px
import pandas as pd
import time

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div( id ='parent', children=[
    html.H1(children='Image Enhancement', style={'textAlign': 'center'}),
    dcc.Upload(
        id='upload-image',
        children=html.Div([
            'Drag and Drop or ',
            html.A('Select Files')
        ]),
        style={
            'width': '100%',
            'height': '60px',
            'lineHeight': '60px',
            'borderWidth': '1px',
            'borderStyle': 'dashed',
            'borderRadius': '5px',
            'textAlign': 'center',
            'margin': '10px',
        },
        # Allow multiple files to be uploaded
        multiple=True
    ),
    html.Div(id='output-image-upload'),
    
 dcc.Loading(id="loading-1",children=[html.Div([html.Div(id="loading-output-1")])], type="circle", style={ 'textAlign': 'center',} ),
 html.Div(
            [
                html.Button('Enhance Image', id='submit-val', n_clicks=0),
                html.Button('Download', id ='download', n_clicks = 0, style = dict(display='none')),
            ],
            style={
                'textAlign': 'center',
            }
            
        ),

])

def parse_contents(contents, filename):
    return html.Div([
        html.H5(filename),
        # HTML images accept base64 encoded strings in the same format
        # that is supplied by the upload
        html.Img(src=contents, style = {'height':'30%', 'width':'30%'}),
        html.Hr(),
    
    ])

@callback(Output('output-image-upload', 'children'),
          #Output('ehanced-image', 'children'),[Input('submit-val', 'n_clicks')],
              Input('upload-image', 'contents'),
              #State('ehanced-image', 'filename'),
              State('upload-image', 'filename', )
)

def update_output(list_of_contents, list_of_names):
    if list_of_contents is not None:
        children = [
            parse_contents(c, n) for c, n in
            zip(list_of_contents, list_of_names)]
        return children
    
#zoom into parts of images 
#fit each image into a set size. ////
#borders around the images
#user should be able to save images 
@callback([Output("loading-output-1", "children"), 
          Output('download', 'children')],
          [ Input("submit-val", "n_clicks")])

def input_triggers_spinner(n_clicks):
    if n_clicks:
        time.sleep(5)
        return dict()
    else:
        return dict(display='none')
        
        



if __name__ == '__main__':
    app.run(debug=True)