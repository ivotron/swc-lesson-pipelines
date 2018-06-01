
import plotly
import xarray as xr
import plotly.plotly as py
from plotly.graph_objs import *
import numpy as np
import os


plotly.tools.set_credentials_file(username=os.environ['PLOTY_USERNAME'], api_key=os.environ['PLOTY_API_KEY'])

print("Loading dataset rasm...")
ds = xr.tutorial.load_dataset('rasm')

print("len: " , len(ds.Tair.xc))

df = ds.Tair.to_dataframe()

print(df.head())

df_sub = df.loc['1980-09-16']

df_sub = df_sub[np.isfinite(df_sub['Tair'])]

data = []
for index, row in df_sub.groupby(level=0):
    data.append(
        Scattermapbox(
            lon=row['xc'],
            lat=row['yc'],
            mode='markers',
            marker=Marker(
                color=row['Tair']
            ),
            hoverinfo='none'
        )
    )

layout = Layout(
    margin=dict(t=0, b=0, r=0, l=0),
    autosize=True,
    hovermode='closest',
    showlegend=False,
    mapbox=dict(
        bearing=0,
        center=dict(
            lat=38,
            lon=-94
        ),
        pitch=0,
        zoom=0,
        style='light'
    ),
)

fig = dict(data=data, layout=layout)

py.image.save_as(fig, filename='data/a-simple-plot.png')

