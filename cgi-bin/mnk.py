#!/usr/bin/env python3

import cgi
import html
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