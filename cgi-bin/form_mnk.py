#!/usr/bin/env python3

import cgi
import html

form = cgi.FieldStorage()
n = form.getfirst("n", "number")
n = html.escape(n)
nint = int(n)

tbl = """<input type="text" name="x0" size="1"> <input type="text" name="y0" size="1"> <br>"""
for i in range(1,nint):
    tbl = tbl + """\n<input type="text" name="x{}" size="1"> <input type="text" name="y{}" size="1"> <br>""".format(str(i), str(i))

print("""Content-type: text/html\n
        <!DOCTYPE HTML>
        <html>
                <head>
                        <meta charset="utf-8">
                        <title>МНК</title>
                </head>
                <body>
                        <form action="mnk.py">
                        Экспериментальные данные:
                        <br>
                        <pre>  X     Y</pre>
                        <br>""",
                        tbl, """
                        <input type="hidden" name="n" value="{}">
                        <input type="submit" value="Далее">
                </body>
        </html>""".format(n))