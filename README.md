# Create a README.md file with the provided documentation

readme_content = """
# Watching You: Software Companies Monitoring System

## Overview
"Watching You: Software Companies" is a web-based application designed to track and log user activities such as searches, video views, likes, comments, and subscriptions. This system also logs user locations and access details in real-time to enhance user behavior analysis. The collected data is stored in a MySQL database for further processing and reporting.

This project is useful for companies aiming to gain insights into user engagement and content preferences on their platforms.

## Features

### User Activity Tracking:
- Logs search queries.
- Tracks video watch history.
- Records likes and comments on content.
- Tracks user subscriptions.

### Real-Time Location Logging:
- Captures user IP addresses and resolves them to geographical locations.
- Stores location information alongside user activity.

### Dynamic Interaction Logging:
- Logs activities instantly as users interact with the website.

### Integration with MySQL Database:
- Stores logs in a well-structured relational database for easy querying and reporting.

---

## System Components

### 1. Backend (Flask Application)
#### Core Functionalities:
- Routes for logging user activities (`/search`, `/watch`, `/like`, `/comment`, `/subscribe`).
- Middleware (`@app.before_request`) to log IP address, access time, and location on every user request.

#### Dependencies:
- **flask**: For web server functionalities.
- **mysql-connector**: For database interaction.
- **datetime**: To capture timestamps.
- **requests**: To fetch geographical location data using an IP geolocation API.

---

### 2. Frontend (HTML and JavaScript)
#### Core Functionalities:
- Dynamic user interaction via JavaScript functions:
  - Search logging.
  - Video view tracking.
  - Content liking and commenting.
  - Subscription logging.
- User-friendly interface with real-time feedback for each interaction.

#### Integration:
- Uses fetch API to send POST requests to backend routes.
- Displays success messages after user actions.

---

### 3. Database (MySQL)
#### Schema Design:
The database consists of the following tables:

| Table Name     | Purpose                                             |
|----------------|-----------------------------------------------------|
| **ip_logs**    | Logs user IP addresses, access times, and locations. |
| **search_logs**| Tracks search queries and their timestamps.         |
| **video_logs** | Logs video views with associated timestamps.        |
| **like_logs**  | Records likes on content.                          |
| **comment_logs** | Stores user comments on content.                  |
| **subscribe_logs** | Logs user subscriptions to channels.            |

---

## Code Details

### 1. Flask Backend

#### Example: Logging Video Views
```python
@app.route('/watch', methods=['POST'])
def watch_video():
    video_id = request.form.get('video_id')
    user_id = request.remote_addr
    location = get_location(user_id)  # Function to fetch location

    cursor = db.cursor()
    cursor.execute(\"""
        INSERT INTO video_logs (user_id, video_id, watch_time)
        VALUES (%s, %s, NOW())
    \""", (user_id, video_id))
    db.commit()

    return jsonify({'status': 'video logged'})



def get_location(ip):
    url = f"http://ip-api.com/json/{ip}"
    response = requests.get(url)
    data = response.json()
    return data.get('city', 'Unknown')




<button onclick="playVideo('video1')">Play Video</button>
<script>
    function playVideo(videoId) {
        fetch('/watch', {
            method: 'POST',
            headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
            body: `video_id=${videoId}`
        }).then(() => {
            document.getElementById('videoMessage').innerText = "Thank You for Watching!";
        });
    }
</script>





CREATE TABLE ip_logs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id VARCHAR(45) NOT NULL,
    access_time DATETIME NOT NULL,
    location VARCHAR(255) NOT NULL
);



CREATE TABLE search_logs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id VARCHAR(50),
    search_query VARCHAR(255),
    search_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);



pip install flask mysql-connector-python requests



git clone https://github.com/your-username/watching-you-software-companies.git
cd watching-you-software-companies




python app.py



 http://127.0.0.1:5000
