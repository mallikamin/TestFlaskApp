from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


import csv
import os

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        ms_number = request.form.get('ms_number')
        latitude = request.form.get('latitude')
        longitude = request.form.get('longitude')

        if not ms_number:
            error = "MS# is required."
            return render_template('form.html', error=error)

        # Save data to CSV file
        file_exists = os.path.isfile('responses.csv')
        with open('responses.csv', 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            if not file_exists:
                # Write header if file doesn't exist
                writer.writerow(['MS#', 'Latitude', 'Longitude'])
            writer.writerow([ms_number, latitude, longitude])

        success_message = f"Form submitted successfully! MS#: {ms_number}, Location: ({latitude}, {longitude})"
        return render_template('success.html', message=success_message)

    return render_template('form.html', error=None)

@app.route('/test-success')
def test_success():
    return render_template('success.html', message="Test success message")



if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
