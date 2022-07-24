from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

url='https://drive.google.com/file/d/1E-GOmtDqSlXEy4ARthIJwzvnmpY56Z0i/view?usp=sharing'
url='https://drive.google.com/uc?id=' + url.split('/')[-2]
df = pd.read_csv(url)
df.dropna(axis=0, inplace=True, how='all')

@app.route("/")
def hello():
	return df.to_html()

@app.route("/search/<name>")
def search_companies(name: str):
	# return df.loc[df["Placed Company name"].str.contains(name, False)].to_json(orient='records')
	return render_template('listing.html', results=df.loc[df["Placed Company name"].str.contains(name, False)].to_dict(orient='records'))

if __name__ == "__main__":
	app.run()
