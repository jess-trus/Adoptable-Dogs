import sqlite3
from flask import Flask, render_template

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('mydatabase.db')
    conn.row_factory = sqlite3.Row
    return conn




@app.route('/')
def index():
    conn = get_db_connection()

    # Get data from the database
    treats_by_state = conn.execute('SELECT contact_city, COUNT(*) as primary_breed FROM treat GROUP BY contact_city').fetchall()

    # Close database connection
    conn.close()

    # Create data arrays for chart.js
    state_labels = [row['contact_city'] for row in treats_by_state]
    treat_counts = [row['primary_breed'] for row in treats_by_state]

    # Create chart.js configuration
    chart_config = {
        'type': 'bar',
        'data': {
            'labels': state_labels,
            'datasets': [{
                'label': 'Number of dogs by City',
                'data': treat_counts,
                'backgroundColor': 'rgba(54, 162, 235, 0.2)',
                'borderColor': 'rgba(54, 162, 235, 1)',
                'borderWidth': 1
            }]
        },
        'options': {
            'scales': {
                'yAxes': [{
                    'ticks': {
                        'beginAtZero': True
                    }
                }]
            }
        }
    }

    # Return the rendered HTML with chart configuration
    return render_template('index.html', chart_config=chart_config)

if __name__ == '__main__':
    app.run(debug=True)