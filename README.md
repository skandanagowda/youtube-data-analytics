# 📊 YouTube Data Analytics Project

This project builds a **semi-automated analytics pipeline** for YouTube data — starting from API extraction to final dashboard visualization.  
It combines **Python**, **AWS Cloud Services**, and **Tableau Public** to generate actionable business insights from YouTube channel metrics.

---

## 🚀 Project Overview

- Extracted video metrics (views, likes, comments, duration, etc.) using the **YouTube Data API** with a Python script.
- Cleaned and transformed raw data using **Pandas**.
- Uploaded the cleaned dataset to an **AWS S3 bucket**.
- Used **AWS Glue** to crawl the data and create a table schema.
- Queried the structured data using **Amazon Athena**.
- Built an interactive **KPI dashboard** using **Tableau Public** to visualize channel performance over time.

---

## 🛠️ Tools & Technologies

- **Python** (Requests, Pandas, Boto3, Dotenv)
- **AWS** (S3, Glue, Athena, IAM)
- **Tableau Public**
- **Git & GitHub**

---

## 📈 Live Dashboard

▶️ [View the Dashboard on Tableau Public](https://public.tableau.com/views/YouTubeAnalytics_17455185008660/YouTubeAnalytics?:language=en-GB&publish=yes&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)

**Example Preview:**

<img width="1075" alt="Dashboard Preview" src="https://github.com/user-attachments/assets/f39cb0f3-54a5-4df0-b7d0-5f14915c22c5" />

---

## 🛠️ Setup Instructions (Python Script Only)

### 1. Clone the repository
```bash
git clone https://github.com/skandanagowda/youtube-data-analytics.git
cd youtube-data-analytics
```
### 2. Create and configure a `.env` file at the project root:
```bash
AWS_ACCESS_KEY_ID=your-access-key
AWS_SECRET_ACCESS_KEY=your-secret-key
AWS_REGION=your-region
YOUTUBE_API_KEY=your-youtube-api-key
BUCKET_NAME=your-s3-bucket-name
KEY_NAME=your-s3-key-name
FILE_NAME=your-local-filename
```
### 3. Install required libraries:
```bash
pip install -r requirements.txt
```

### 4. Run the Python scripts in order:
- Step 1: Extract YouTube Data
```bash
python youtube_api_script.py
```
(Fetches video data from YouTube Data API and saves to CSV)

- Step 2: Clean the Raw Data
```bash
python clean_data.py
```
(Cleans and formats the CSV for analysis)

- Step 3: Upload Cleaned Data to S3
```bash
python upload_to_s3.py
```
(Uploads the final cleaned CSV to your S3 bucket)

After these steps, you can proceed with AWS Glue, Athena, and Tableau.

🎯 **Additional Notes**
- Sensitive credentials (like the `.env` file) are excluded from GitHub for security reasons.
- This project does not automate the Glue crawler or Athena queries yet — semi-automated for now.
- Tableau Public dashboard is manually linked to Athena using a live JDBC connection for KPIs and trends.

📈 **Visualization with Tableau**
- Connected AWS Athena to Tableau Desktop (Free Trial) using a JDBC driver.
- Queried KPIs like total views, likes, comments, most viewed year, and videos per year directly from Athena.
- Built a fully interactive and professional Tableau Business Dashboard.
- Published the dashboard to Tableau Public for live online access.

🔗 **Project Links**
- [GitHub Repository](https://github.com/skandanagowda/youtube-data-analytics)
- [Tableau Public Dashboard](https://public.tableau.com/views/YouTubeAnalytics_17455185008660/YouTubeAnalytics?:language=en-GB&publish=yes&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)

🙌 **Acknowledgements**

Special thanks to free APIs, AWS Free Tier, and Tableau Public for making this possible.
