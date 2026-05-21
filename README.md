News Sentiment Analysis Pipeline
__________________________________
This project is an end-to-end News Sentiment Analysis Data Pipeline built using Python, PostgreSQL, AWS Lambda, S3, ECR, ECS Fargate, Docker, and Streamlit.
The pipeline automatically collects news articles from the News API, performs sentiment analysis, stores processed data in PostgreSQL (Amazon RDS), saves raw JSON files in Amazon S3, and displays analytics through a Streamlit dashboard deployed on AWS ECS Fargate.

FeatureS
___________
*Automated News Collection
*Sentiment Analysis
*PostgreSQL Data Storage
*Raw JSON Backup in S3
*Dockerized Deployment
*Live Streamlit Dashboard
*Fully Cloud Deployed on AWS

Architecture
______________
docs/news_flowchart.jpeg

Workflow
___________
1.AWS EventBridge triggers AWS Lambda every 5 minutes
2.Lambda Function:
  Fetches news articles from News API
  Performs sentiment analysis
  Stores processed data in PostgreSQL RDS
  Saves raw JSON files into S3
3.Amazon RDS PostgreSQL stores structured news data
4.Amazon S3 stores raw news JSON files
5.Dockerized Streamlit Dashboard is pushed to Amazon ECR
6.Amazon ECS Fargate runs the Streamlit container
7.Users access the dashboard through ECS public endpoint

Technologies Used
__________________
*Python
*News API
*PostgreSQL
*AWS Lambda
*AWS EventBridge
*Amazon RDS
*Amazon S3
*Docker
*Amazon ECR
*Amazon ECS Fargate
*Streamlit

Project Structure
____________________

NEWS-API-Project/
│
├── docker/
│   └── dockerfile
│
├── docs/
│   └── news_flowchart.jpeg
│
├── lambda/
│   ├── modules/
│   │   ├── rdsupload.py
│   │   └── s3upload.py
│   │
│   └── lambda_function.py
│
├── news_test/
│   └── test_api.py
│
├── news_test_data/
│   └── news.json
│
├── packages/
│
├── streamlit_app/
│   └── streamlitapp.py
│
├── venv/
│
├── .env
├── .gitignore
├── README.md
└── requirements.txt


Table Creation
_______________
CREATE TABLE IF NOT EXISTS news_data (
    id SERIAL PRIMARY KEY,
    author TEXT,
    published_date TIMESTAMP,
    description TEXT,
    sentiment_score FLOAT
)

Run lambda scripts Locally
____________________________
python lambda_function.py

Run streamlit Dashboard
___________________________
streamlit run streamlitapp.py

Docker Build
______________

*Build Docker Image
  docker build -t news-dashboard .

*Run Docker Container
  docker run -p 8501:8501 news-dashboard

AWS Deployment
___________________
Push Docker image to Amazon ECR:
 aws ecr get-login-password --region your-region | docker login --username AWS --password-stdin your-ecr-uri

 docker tag news-dashboard:latest your-ecr-uri/news-dashboard

 docker push your-ecr-uri/news-dashboard


Deploy to ECS Fargate
_______________________
Create ECS Cluster
Create Task Definition
Add Container
Configure Port 8501
Create ECS Service
Enable Public IP
Access Dashboard using ECS Public URL

Dashboard
___________
The Streamlit dashboard displays:
 Latest News Articles
 Sentiment Scores
 Positive / Negative Analysis
 News Trends
 Interactive Visualizations

Author
________
Gopika C 