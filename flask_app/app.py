import sqlite3
from flask import Flask, render_template
import os

app = Flask(__name__)

# Setting connection to the sqlite database
def get_db_connection():
    conn = sqlite3.connect('mydatabase.db')
    conn.row_factory = sqlite3.Row
    return conn



# Create app routes for each page on website

@app.route('/chart')
def get_chart():
    conn = get_db_connection()

    # Get data from the database
    treats_by_state = conn.execute('SELECT breed_primary, COUNT(*) as name FROM treat GROUP BY breed_primary').fetchall()

    # Close database connection
    conn.close()

    # Create data arrays for chart.js
    state_labels = [row['breed_primary'] for row in treats_by_state]
    treat_counts = [row['name'] for row in treats_by_state]

    # Create chart.js configuration
    chart_config = {
        'type': 'bar',
        'data': {
            'labels': state_labels,
            'datasets': [{
                'label': 'Number of Dogs by Breed',
                'data': treat_counts,
                'backgroundColor': 'rgba(54, 162, 235, 0.2)',
                'borderColor': 'rgba(54, 162, 235, 1)',
                'borderWidth': 1
            }]
        },
        'options': {
            'responsive': True
         }
};

    # Return the rendered HTML with chart configuration
    return render_template('chart.html', chart_config=chart_config)

@app.route('/')
def index():
    return render_template('index.html', title='Adopt a Dog- New Jersey')

@app.route('/info')
def get_info():
    return render_template('info.html', title='Adopt a Dog- New Jersey')

@app.route('/map')
def get_map():
    return render_template('map.html')

if __name__ == '__main__':
    app.run(debug=True)