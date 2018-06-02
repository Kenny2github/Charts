import os
from subprocess import check_output
import chparse

if check_output(('git', 'rev-parse', '--abbrev-ref', 'HEAD')).decode('utf8').strip() == 'gh-pages':
	raise SystemExit(0)

conts = """<html>
<head>
	<title>Kenny2minecraft's Charts</title>
	<style>
		body {
			background-color: darkblue;
			color: white;
			font-family: monospace;
		}
		table {
			width: 100%;
		}
	</style>
	<link rel="shortcut icon" href="/index/favicon.ico" type="image/x-icon"/>
</head>
<body>
	<h1>Kenny2minecraft's Charts</h1>
	<p>Welcome! This page just lists the charts I've made.</p>
	<table>
		<tr><th>Song Name</th><th>Artist</th><th>Genre</th><th>Charter</th><th>Album</th></tr>
"""

for d in os.listdir():
	if os.path.isdir(d) and not d.startswith('.'):
		with open(os.path.join(d, 'notes.chart')) as f:
			chart = chparse.load(f)
			conts += """<tr><td>{0.Name}</td><td>{0.Artist}</td><td>{0.Genre}</td><td>{0.Charter}</td><td>{1}</td></tr>
""".format(chart, getattr(chart, 'Album', ''))
conts += """	</table>
</body>
</html>
"""
os.system('git checkout gh-pages>nul')
with open('index.html', 'w') as f:
	f.write(conts)
os.system('git commit -am "Update charts page">nul')
os.system('git push origin gh-pages>nul')
os.system('git checkout master>nul')
