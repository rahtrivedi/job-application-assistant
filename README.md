SmartApply Assistant

SmartApply Assistant is a personal job application automation tool that helps applicants extract data from job advertisements, generate multilingual cover letters, track applications, and optionally prepare emails via Gmail integration.

This project is designed for engineers, developers, and professionals who apply to many positions and want to streamline their workflow without losing personalization.

🚀 Features

🔍 Job Advertisement Scraping

Extracts key information from job ads (title, company, location, reference number, contact person, email)

Supports structured HTML job portals (e.g. Arbeitsagentur)

✍️ Cover Letter Generation

Automatically generates personalized cover letters

Supports multiple languages (DE / EN)

Adapts salutation based on detected contact person (Herr / Frau)

📊 Application Tracking

Stores structured job data in Excel

Easy to track applied positions, companies, and references

📧 Email Preparation (Optional)

Prepares Gmail drafts using Gmail API

User can review and approve emails before sending

Supports file attachments (CV, cover letter, certificates)

🧠 Manual Override

Allows manual input when job data is incomplete or missing

Ensures flexibility and correctness

🛠️ Tech Stack

Python

BeautifulSoup (bs4) – HTML parsing & scraping

Google Gmail API – email draft automation

Git / GitHub – version control

Excel (XLSX) – application tracking

OAuth 2.0 – secure Gmail authentication

📂 Project Structure
JobApplication/
│
├── page.html                  # Sample job ad HTML
├── main.py                    # Main automation script
├── gmail_auth.py              # Gmail OAuth authentication
├── anschreibungV1.py          # Cover letter generator
├── credentials.json           # Google OAuth credentials (ignored)
├── token.json                 # OAuth token (auto-generated)
├── applications.xlsx          # Application tracking file
└── README.md

🔐 Gmail Authentication

Uses OAuth 2.0

Authentication is required only once

Token is stored locally (token.json)

App works in test mode with approved Gmail user

Emails are created as drafts by default to avoid spam risks.

📌 Use Case

This tool is ideal for:

Job seekers applying to multiple roles

Engineers transitioning into new domains

Applicants who want automation with control

Developers building a real-world portfolio project

⚠️ Disclaimer

This project is intended for personal use

Mass unsolicited emailing is discouraged

Always review generated content before sending

📈 Future Improvements

Support for more job portals

UI (Web or Desktop)

Resume parsing

ATS keyword optimization

Multi-account email support

👤 Author

Rahul Kumar Trivedi
Mechanical Engineer → BIM / Software Development
📍 Germany
