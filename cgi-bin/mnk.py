#!/usr/bin/env python3

import cgi
import html
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px
import pandas as pd

form = cgi.FieldStorage()
n = form.getfirst("n", "number")
n = html.escape(n)
nint = int(n)
xlist = []
ylist = []
for i in range(0, nint):
	xname = "x{}".format(str(i))
	x = form.getfirst(xname, "x value")
	x = html.escape(x)
	xfloat=float(x.replace(',', '.'))
	xlist.append(xfloat)
	yname = "y{}".format(str(i))
	y = form.getfirst(yname, "y value")
	y = html.escape(y)
	yfloat=float(y.replace(',', '.'))
	ylist.append(yfloat)

df = pd.DataFrame(xlist, ylist)
fig = px.scatter(df, trendline="ols")
fig.show()

'''
html_str = """Content-type: text/html\n
        <!DOCTYPE HTML>
        <html>
                <head>
                        <meta charset="utf-8">
                        <title>МНК</title>
                </head>
                <body>
                	
                </body>
        </html>"""

#<form action="graph.py">
#                <input type="submit" value="Далее">

print(html_str)
'''