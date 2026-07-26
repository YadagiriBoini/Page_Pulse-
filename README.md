# 🚀 Page Pulse

Page Pulse is a simple web application that audits any webpage and returns key SEO and performance metrics.

Built as part of the **Digital Heroes Software Development Engineering Internship Task**.

---

## Features

- ✅ HTTP Status Code
- ⚡ Response Time
- 📄 Page Title
- 📝 Meta Description
- 🔠 H1 Count
- 🖼 Images Missing Alt Text
- 📚 Approximate Word Count
- ❌ Handles Invalid URLs
- ⏱ Handles Timeouts
- 📑 Detects Non-HTML Pages

---

## Tech Stack

### Frontend
- HTML
- CSS
- JavaScript

### Backend
- Python
- Flask
- Requests
- BeautifulSoup4

---

## Project Structure

```
page-pulse/
│
├── app.py
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
|   |__ script.js
│
├── README.md
```

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/page-pulse.git
```

### 2. Move into the project

```bash
cd page-pulse
```

### 3. Create a virtual environment

Windows

```bash
python -m venv venv
venv\Scripts\activate
```

Mac/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install flask requests beautifulsoup4 pytest 
```

### 5. Start the application

```bash
python app.py
```

Open your browser and visit

```
http://127.0.0.1:5000
```

---

# API

## POST /analyze

Accepts a webpage URL and returns the audit report.

### Request

```json
{
    "url":"https://example.com"
}
```

### Success Response

```json
{
    "status":200,
    "response_time":"383 ms",
    "title":"Example Domain",
    "meta_description":"No description",
    "h1_count":1,
    "missing_alt":0,
    "word_count":21
}
```

### Error Response

```json
{
    "error":"Invalid URL"
}
```

Possible errors

- Invalid URL
- Timeout
- Non-HTML Page
- Website Unreachable

---

# Running Tests

Run the tests using

```bash
pytest
```

Included test cases

- ✅ Valid webpage
- ❌ Invalid URL
- ❌ Non-HTML page

---

# Design Decisions

### 1. Flask for Backend

Flask was selected because it is lightweight, easy to configure, and well-suited for creating a simple REST API for webpage analysis.

---

### 2. BeautifulSoup for HTML Parsing

BeautifulSoup simplifies extracting HTML elements such as the page title, meta description, headings, images, and text content without requiring a browser automation tool.

---

### 3. Requests Library for Fetching Pages

The Requests library was chosen to measure response time and retrieve webpage content efficiently while supporting timeout handling and HTTP status inspection.

---

# Error Handling

The application gracefully handles

- Invalid URLs
- Connection failures
- Request timeouts
- Non-HTML responses
- Missing metadata

---

# Sample Output

```
HTTP Status: 200
Response Time: 383 ms
Title: Example Domain
Meta Description: No description
H1 Count: 1
Images Missing Alt: 0
Word Count: 21
```

---

# Future Improvements

- Lighthouse integration
- SEO score calculation
- Download report as PDF
- Export report as JSON
- Accessibility audit
- Mobile-friendly analysis

---

# Footer Requirement

Built for **Digital Heroes Training Task**

---

## Author

Boini Yadagiri

GitHub:
