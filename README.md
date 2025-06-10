# Morocco Water Scarcity Solution - Complete System Documentation

## Overview

This comprehensive solution addresses water scarcity challenges in Morocco through a two-application system:

1. **AI Backend Service**: Automatically gathers water-related information and generates AI-powered reports
2. **Web Frontend Application**: Provides user interface for accessing reports, community engagement, and user management

The system combines real-time data collection, AI analysis, and community participation to tackle Morocco's water scarcity issues.

## Problem Statement

Morocco faces significant water scarcity challenges that require continuous monitoring and analysis. This application provides automated intelligence gathering and report generation to help understand current water situations and provide actionable insights.

## System Architecture

The solution consists of two separate applications that work together:

### Application 1: AI Backend Service (Port 5000)
```
Ai_app/
├── services/           # Core business logic
│   ├── quiz_service.py
│   └── report_service.py
├── utils/             # Utility functions
│   ├── google_search.py
│   └── prompt_templates.py
├── config.py          # Configuration settings
├── main.py           # Flask API server
├── app.ipynb         # Jupyter notebook interface
└── .env              # Environment variables
```

### Application 2: Web Frontend (Port 5002)
```
myProject/
├── game/              # Game functionality
│   └── reutres.py
├── main/              # Main application routes
│   └── route.py
├── static/            # Static assets (CSS, JS, images)
├── templates/         # HTML templates
│   ├── login.html     # Login page
│   ├── registre.html  # Registration page
│   ├── base.html      # Base template
│   ├── create.html    # Content creation
│   ├── about.html     # About/donation page
│   ├── rapore.html    # AI reports display
│   ├── jeu.html       # Game interface
│   └── [other templates]
├── __init__.py        # App factory
├── config.py          # Configuration
├── form.py           # WTForms definitions
├── model.py          # Database models
├── routes.py         # Route definitions
├── app.py            # Application entry point
└── requirements.txt   # Dependencies
```

## Core Features

### AI Backend Service Features

#### 1. Data Collection
- **Google Search Integration**: Uses Google Search API to scrape internet data
- **Targeted Sources**: Focuses on government websites and news outlets
- **Time-based Filtering**: Collects information from the last week
- **Morocco-specific**: Tailored to Moroccan water situation data

#### 2. AI-Powered Analysis
- **Llama3 Integration**: Leverages Llama3 model for report generation
- **Comprehensive Reports**: Generates detailed analysis including:
  - Current water situation assessment
  - Problem identification and analysis
  - Suggested solutions and recommendations
  - Actionable steps for improvement

#### 3. API Interface
- **RESTful API**: Clean Flask-based API for frontend consumption
- **JSON Response**: Structured data format for easy integration
- **Error Handling**: Robust error management and reporting

### Web Frontend Features

#### 1. User Management System
- **User Registration**: Secure user registration with email validation
- **User Authentication**: Login system with password hashing
- **User Profiles**: Store user information (name, phone, address, email)
- **Session Management**: Flask-Login integration for user sessions

#### 2. Report Viewing Interface
- **AI Report Display**: View generated water scarcity reports
- **Real-time Data**: Access to latest AI-generated analysis
- **User-friendly Interface**: Clean presentation of complex data

#### 3. Community Engagement Game
- **Monthly Video Submission**: Users can upload videos explaining water situation in their area
- **Random Number Game**: Simple game mechanic to select monthly winner
- **Community Participation**: Encourages local water situation reporting
- **User-generated Content**: Collect real-world water scarcity experiences

#### 4. Information & Donation Hub
- **About Page**: Information about water scarcity in Morocco
- **Donation Information**: Resources for people wanting to help
- **Educational Content**: Raise awareness about water conservation

## API Documentation

### AI Backend Service (Port 5000)

#### Base URL
```
http://localhost:5000
```

#### Endpoints

##### Generate Water Scarcity Report
- **URL**: `/generate_report`
- **Method**: `GET`
- **Description**: Generates a comprehensive water scarcity report for Morocco

**Response Format**:
```json
{
  "report": {
    "situation_analysis": "Current water situation in Morocco...",
    "identified_problems": ["Problem 1", "Problem 2", "..."],
    "suggested_solutions": ["Solution 1", "Solution 2", "..."],
    "actionable_steps": ["Step 1", "Step 2", "..."],
    "data_sources": ["Source 1", "Source 2", "..."],
    "generated_at": "2025-06-10T10:30:00Z"
  }
}
```

**Error Response**:
```json
{
  "error": "Error description"
}
```

### Web Frontend Application (Port 5002)

#### Base URL
```
http://localhost:5002
```

#### Main Routes

##### Authentication Routes
- **URL**: `/` (Login Page)
- **Method**: `GET, POST`
- **Description**: User login interface

- **URL**: `/register`
- **Method**: `GET, POST`
- **Description**: User registration interface

##### Application Routes
- **URL**: `/home`
- **Method**: `GET`
- **Description**: Main dashboard (requires authentication)

- **URL**: `/rapore`
- **Method**: `GET`
- **Description**: Display AI-generated water reports

- **URL**: `/jeu`
- **Method**: `GET, POST`
- **Description**: Community engagement game interface

- **URL**: `/about`
- **Method**: `GET`
- **Description**: Information and donation page

## Installation & Setup

### Prerequisites
- Python 3.8+
- Google Search API credentials
- Llama3 model access
- SQLite/PostgreSQL for database
- Required Python packages

### Setup Instructions

#### 1. AI Backend Service Setup

**Navigate to AI app directory**:
```bash
cd WaterVoice-Ibn-Tofail-Hackaton
```

**Install dependencies**:
```bash
pip install -r requirements.txt
```

**Configure environment variables** (`.env`):
```env
# Google Search API
GOOGLE_API_KEY=your_google_api_key
GOOGLE_CSE_ID=your_custom_search_engine_id

# Llama3 Configuration
LLAMA3_API_KEY=your_llama3_api_key
LLAMA3_MODEL_NAME=llama3-model-name

# Application Settings
FLASK_ENV=development
FLASK_DEBUG=True
```

**Start the AI backend**:
```bash
python3 main.py
```
*AI service will run on port 5000*

#### 2. Web Frontend Setup

**Navigate to frontend directory**:
```bash
cd myProject
```

**Start the web application**:
```bash
python app.py
```
*Web application will run on port 5002*

### Complete System Startup

1. **Start AI Backend** (Terminal 1):
```bash
cd Ai_app
python main.py
```

2. **Start Web Frontend** (Terminal 2):
```bash
cd myProject
python app.py
```

3. **Access the application**:
   - Frontend: `http://localhost:5002`
   - AI API: `http://localhost:5000`

## Core Components

### AI Backend Components

#### Google Search Integration (`utils/google_search.py`)
```python
from langchain_google_community import GoogleSearchAPIWrapper

def search_google(query: str):
    search = GoogleSearchAPIWrapper()
    return search.run(query)
```
**Purpose**: Scrapes internet data from government websites and news sources about Morocco's water situation.

#### Report Generation Service (`services/report_service.py`)
- Processes collected data
- Interfaces with Llama3 AI model
- Generates structured reports with analysis and recommendations

#### Prompt Templates (`utils/prompt_templates.py`)
- Contains optimized prompts for Llama3
- Ensures consistent report structure
- Guides AI analysis focus areas

### Web Frontend Components

#### User Authentication (`main/route.py`)
```python
@main.route('/',methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('route.home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for('route.home'))
    return render_template("login.html", title="Login", form=form)
```

#### User Registration System
- **Email Validation**: Uses `email_validator` for proper email format checking
- **Duplicate Prevention**: Checks for existing emails and phone numbers
- **Password Security**: Uses bcrypt for password hashing
- **Database Integration**: SQLAlchemy models for user data

#### Application Entry Point (`app.py`)
```python
from myProject import create_app, db
from flask_migrate import Migrate

app = create_app()
migrate = Migrate(app, db)

if __name__ == "__main__":
    app.run(debug=True, port=5002)
```

#### Database Models (`model.py`)
- **User Model**: Stores user registration information
- **Database Relationships**: Designed for user management and content association
- **Migration Support**: Flask-Migrate integration for database schema updates

## Usage Examples

### AI Backend Usage

#### Basic API Call
```bash
curl -X GET http://localhost:5000/generate_report
```

#### Python Integration
```python
import requests

response = requests.get('http://localhost:5000/generate_report')
report_data = response.json()

print(f"Water Situation: {report_data['report']['situation_analysis']}")
print(f"Solutions: {report_data['report']['suggested_solutions']}")
```

### Web Frontend Usage

#### User Registration Flow
1. Navigate to `http://localhost:5002/register`
2. Fill out registration form with:
   - First Name and Last Name
   - Phone Number (unique)
   - Address
   - Email (unique, validated)
   - Password (hashed)
3. Submit form to create account
4. Redirect to login page upon success

#### User Login Flow
1. Navigate to `http://localhost:5002/` (login page)
2. Enter registered email and password
3. Optional: Check "Remember Me" for persistent sessions
4. Redirect to home dashboard upon successful authentication

#### Accessing AI Reports
1. Log in to the web application
2. Navigate to Reports page (`/rapore`)
3. View latest AI-generated water scarcity reports
4. Reports are fetched from AI backend service in real-time

#### Community Game Participation
1. Navigate to Game page (`/jeu`)
2. Participate in monthly random number guessing game
3. Winner gets opportunity to upload video about local water situation
4. Contribute to community-driven water scarcity documentation

## System Integration

### Frontend-Backend Communication

The web frontend integrates with the AI backend through HTTP requests:

#### Report Integration
```python
# Example: Fetching AI reports in frontend
import requests

def get_latest_report():
    try:
        response = requests.get('http://localhost:5000/generate_report')
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": "Failed to fetch report"}
    except Exception as e:
        return {"error": str(e)}
```

#### Frontend Route Example
```python
@app.route('/rapore')
@login_required
def view_reports():
    report_data = get_latest_report()
    return render_template('rapore.html', report=report_data)
```

### Game System Flow

1. **Random Number Generation**: System generates random number monthly
2. **User Participation**: Users submit guesses through web interface
3. **Winner Selection**: First correct guess wins
4. **Video Upload**: Winner gets video upload privileges
5. **Community Content**: Videos shared with community for awareness

### Database Schema

#### User Model Structure
```python
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    numero = db.Column(db.String(20), unique=True, nullable=False)
    address = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
```

## Troubleshooting

### AI Backend Issues

#### Common Issues

1. **Google API Rate Limits**
   - Monitor API usage
   - Implement rate limiting
   - Use caching for repeated queries

2. **Llama3 Connection Issues**
   - Verify API credentials
   - Check network connectivity
   - Monitor model availability

3. **No Recent Data Found**
   - Adjust search time range
   - Expand search terms
   - Check source availability

### Web Frontend Issues

#### Authentication Problems

1. **Login Failed**
   - Verify email format and password
   - Check user exists in database
   - Ensure password hashing is consistent

2. **Registration Issues**
   - Email already exists error
   - Phone number uniqueness validation
   - Email format validation errors

#### Database Issues

1. **Migration Errors**
   ```bash
   # Reset migrations if needed
   rm -rf migrations/
   flask db init
   flask db migrate -m "Initial migration"
   flask db upgrade
   ```

2. **Database Connection**
   - Check database file permissions
   - Verify database configuration
   - Ensure SQLite/PostgreSQL is properly installed

#### Integration Issues

1. **AI Service Unreachable**
   - Verify AI backend is running on port 5000
   - Check network connectivity between services
   - Validate API endpoint URLs

2. **Report Display Problems**
   - Check AI service response format
   - Verify JSON parsing in frontend
   - Handle API timeout scenarios

### Logging and Debugging

#### AI Backend Logging
- Application logs available in console output
- Error tracking for API requests
- Search query and response logging

#### Frontend Logging
- Flask debug mode for development
- User authentication logging
- Database query logging
- Template rendering errors

## System Workflow

### Complete User Journey

1. **User Registration**
   - User visits web application (`localhost:5002`)
   - Registers with personal information
   - Account created with secure password hashing

2. **Authentication**
   - User logs in with email/password
   - Session management handles authentication state
   - Access to protected routes granted

3. **Report Access**
   - User navigates to Reports page
   - Frontend requests latest data from AI backend
   - AI service scrapes recent water data from internet
   - Llama3 generates comprehensive analysis
   - Report displayed to user through web interface

4. **Community Participation**
   - User participates in monthly guessing game
   - Winner selected based on random number
   - Video upload opportunity for local water situation
   - Community content contributes to awareness

5. **Information & Action**
   - User accesses About page for additional information
   - Donation resources provided for those wanting to help
   - Educational content raises awareness

### Technical Data Flow

```
Internet Sources → Google Search API → AI Backend → Llama3 → Generated Report
                                          ↓
User Registration → Web Frontend → Authentication → Report Display
      ↓                              ↓
Database Storage ← User Management ← Game System
```

---
**▶️ Live Demo:** [Experience the system](https://drive.google.com/file/d/1UQqmEdlQa-WJqnUl8x5Ya1ZlvDTSdA_-/view?usp=sharing)
