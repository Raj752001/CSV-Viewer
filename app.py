from flask import Flask, render_template, request, redirect, url_for
import pandas as pd

app = Flask(__name__)

url='https://drive.google.com/file/d/1E-GOmtDqSlXEy4ARthIJwzvnmpY56Z0i/view?usp=sharing'
url='https://drive.google.com/uc?id=' + url.split('/')[-2]
df = pd.read_csv(url)
df = df.dropna(axis=0, how='all').reset_index()

@app.route("/")
def home_page():
    return render_template('listing.html', results=df.to_dict(orient='records'), heading='All Experiences')

@app.route("/search")
def search_companies():
    name = request.args.get('name')
    if name is None:
        return redirect(url_for('home_page'))
    return render_template('listing.html', results=df.loc[df["Placed Company name"].str.contains(name, False)].to_dict(orient='records'), heading = 'Search Results: ' + name)

@app.route("/experience/<index>")
def view_experience(index):
    return render_template('experience.html', result=df.iloc[int(index), 2:].to_dict())

if __name__ == "__main__":
    app.run()
