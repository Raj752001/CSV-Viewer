from flask import Flask, render_template, request, redirect, url_for
import pandas as pd

app = Flask(__name__)

url='https://drive.google.com/file/d/1E-GOmtDqSlXEy4ARthIJwzvnmpY56Z0i/view?usp=sharing'
url='https://drive.google.com/uc?id=' + url.split('/')[-2]
df = pd.read_csv(url)
df = df.dropna(axis=0, how='all').reset_index()

@app.route("/")
def home_page():
    '''List of all experiences'''
    companies = list(df['Placed Company name'].unique())
    return render_template('listing.html', results=df.to_dict(orient='records'), heading='All Experiences', companies=companies)

@app.route("/search")
def search_companies():
    '''Gets the list of experiences according to searched company name'''
    name = request.args.get('name')
    if name is None:
        return redirect(url_for('home_page'))
    companies = list(df['Placed Company name'].unique())
    return render_template('listing.html', results=df.loc[df["Placed Company name"].str.contains(name, False)].to_dict(orient='records'), heading = 'Search Results: ' + name, compaines=companies)

@app.route("/experience/<index>")
def view_experience(index):
    '''A view to show a single experience in detail'''
    companies = list(df['Placed Company name'].unique())
    return render_template('experience.html', result=df.iloc[int(index), 2:].to_dict(), companies=companies)

if __name__ == "__main__":
    app.run()
