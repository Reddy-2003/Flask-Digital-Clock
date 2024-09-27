from flask import Flask, render_template, request
import pytz
from datetime import datetime

app = Flask(__name__)

# Mapping of countries to their respective time zones
country_timezones = {
    "United States": "America/New_York",
    "Canada": "America/Toronto",
    "United Kingdom": "Europe/London",
    "Germany": "Europe/Berlin",
    "Australia": "Australia/Sydney",
    "India": "Asia/Kolkata",
    "Japan": "Asia/Tokyo",
    "Singapore": "Asia/Singapore",
    "China": "Asia/Shanghai",
    "Brazil": "America/Sao_Paulo",
    # Add more countries and their time zones as needed
}

@app.route('/', methods=['GET', 'POST'])
def clock():
    selected_country = request.form.get('country', 'United States')  # Default to United States
    timezone = country_timezones.get(selected_country, 'UTC')
    
    # Get current time in the selected time zone
    tz = pytz.timezone(timezone)
    current_time = datetime.now(tz).strftime("%I:%M:%S %p")  # Format with AM/PM
    
    return render_template('clock.html', current_time=current_time, country=selected_country, country_timezones=country_timezones)

@app.route('/time', methods=['GET'])
def get_time():
    timezone = request.args.get('timezone', 'UTC')
    tz = pytz.timezone(timezone)
    current_time = datetime.now(tz).strftime("%I:%M:%S %p")  # Format with AM/PM
    return current_time

if __name__ == '__main__':
    app.run(debug=True)
