from flask import Flask, render_template_string
import pandas as pd
import subprocess

app = Flask(__name__)

@app.route('/')
def home():
    # Read the CSV file
    try:
        df = pd.read_csv("barge_data.csv")
    except Exception as e:
        return f"<h1>Error loading data</h1><p>{e}</p>"

    # Group by lock and direction, summing barge counts
    summary = df.groupby(["Lock Name", "Direction"])["Barge Count"].sum().reset_index()

    # Convert to HTML table
    table_html = summary.to_html(index=False)

    html = f'''
    <html>
    <head>
        <title>SWW Barge Tracker</title>
        <style>
            body {{ font-family: Arial, sans-serif; padding: 40px; }}
            table {{ border-collapse: collapse; width: 60%; }}
            th, td {{ border: 1px solid #ccc; padding: 8px; text-align: center; }}
            th {{ background-color: #f2f2f2; }}
        </style>
    </head>
    <body>
        <h1>SWW Barge Tracker</h1>
        <p>Daily barge counts by lock and direction</p>
        {table_html}
    </body>
    </html>
    '''
    return render_template_string(html)

@app.route('/run-update')
def run_update():
    try:
        subprocess.run(['python3', 'update_barge_data.py'], check=True)
        return "✅ Data updated!"
    except Exception as e:
        return f"❌ Failed to update: {e}"

app.run(host='0.0.0.0', port=81)