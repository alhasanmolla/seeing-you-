import requests
from flask import Flask, render_template, request
import mysql.connector
from datetime import datetime

app = Flask(__name__)

# Set up MySQL connection
db = mysql.connector.connect(
    host="localhost",
    user="root",  # Update with your MySQL username
    password="12345",  # Update with your MySQL password
    database="website_activity"
)

# Cursor for executing SQL queries
cursor = db.cursor()

# Geolocation API URL (Using ipinfo.io as an example, you can replace with another geolocation API if you prefer)
GEO_API_URL = "https://ipinfo.io/json"  # You can sign up for an API key if needed

# Function to get user's location based on IP
def get_user_location(ip_address):
    try:
        # Make a request to the geolocation API to get details based on IP address
        response = requests.get(f"https://ipinfo.io/{ip_address}/json")
        location_data = response.json()
        location = location_data.get('city', 'Unknown')  # Default to 'Unknown' if no city found
        return location
    except requests.exceptions.RequestException as e:
        print(f"Error fetching geolocation: {e}")
        return 'Unknown'

@app.route('/')
def index():
    # Get user's IP address
    user_ip = request.remote_addr
    
    # Get the location of the user based on their IP address
    location = get_user_location(user_ip)
    
    # Log the user's IP and location in the database
    user_id = 'user1'  # This can be dynamically set based on your user authentication
    access_time = datetime.now()

    cursor.execute("INSERT INTO ip_logs (user_id, access_time, location) VALUES (%s, %s, %s)",
                   (user_id, access_time, location))
    db.commit()

    print(f"User IP: {user_ip}, Location: {location}")  # You can log this for debugging

    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    user_id = 'user1'  # This should be dynamically set based on session or user
    search_query = request.form.get('search_query')
    search_time = datetime.now()

    cursor.execute("INSERT INTO search_logs (user_id, search_query, search_time) VALUES (%s, %s, %s)",
                   (user_id, search_query, search_time))
    db.commit()
    return '', 200

@app.route('/watch', methods=['POST'])
def watch():
    user_id = 'user1'  # This should be dynamically set
    video_id = request.form.get('video_id')
    watch_time = datetime.now()

    cursor.execute("INSERT INTO video_logs (user_id, video_id, watch_time) VALUES (%s, %s, %s)",
                   (user_id, video_id, watch_time))
    db.commit()
    return '', 200

@app.route('/like', methods=['POST'])
def like():
    user_id = 'user1'  # This should be dynamically set
    content_id = request.form.get('content_id')
    like_time = datetime.now()

    cursor.execute("INSERT INTO like_logs (user_id, content_id, like_time) VALUES (%s, %s, %s)",
                   (user_id, content_id, like_time))
    db.commit()
    return '', 200

@app.route('/comment', methods=['POST'])
def comment():
    user_id = 'user1'  # This should be dynamically set
    content_id = request.form.get('content_id')
    comment_text = request.form.get('comment_text')
    comment_time = datetime.now()

    cursor.execute("INSERT INTO comment_logs (user_id, content_id, comment_text, comment_time) VALUES (%s, %s, %s, %s)",
                   (user_id, content_id, comment_text, comment_time))
    db.commit()
    return '', 200

@app.route('/subscribe', methods=['POST'])
def subscribe():
    user_id = 'user1'  # This should be dynamically set
    channel_id = request.form.get('channel_id')
    subscribe_time = datetime.now()

    cursor.execute("INSERT INTO subscribe_logs (user_id, channel_id, subscribe_time) VALUES (%s, %s, %s)",
                   (user_id, channel_id, subscribe_time))
    db.commit()
    return '', 200

if __name__ == '__main__':
    app.run(debug=True)
