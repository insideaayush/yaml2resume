# yaml2resume: YAML → HTML Resume Generator

A simple, ATS-friendly **resume generator** that converts a structured `resume.yaml` file into a beautiful and printable **HTML resume**. Built with clean CSS, designed for recruiter readability and modern ATS systems.

---

## Features

- Generates a **single-column, ATS-compliant** resume in HTML
- Accepts structured **YAML** format (schema defined below)
- Uses **clean HTML + CSS** — easily printable or exportable to PDF
- Modular and reusable code (easy to extend for PDF or DOCX output)
- Ideal for **developers**, **open source contributors**, and anyone who prefers data-driven documents

---

## 🔧 Usage

### 🖥️ Local Setup

```bash
git clone https://github.com/insideaayush/yaml2resume.git
cd yaml2resume

# (Optional) create a virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependency
pip install -r requirements.txt

# Run the script
python yaml2resume.py
```

This will generate `sample/sample.html` from `sample/sample.yaml`.

---

## equirements

- Python 3.7+
- requirements.txt lists all the packages required!

Install it with:

```bash
pip install -r requirements.txt 
```

---

## ✍️ YAML Resume Schema

Your YAML file should follow this structure:

```yaml
name: Your Name
tagline: Your Professional Title

contact:
  email: your.email@example.com
  phone: "+65-00000000"
  location: Your City, Country
  linkedin: https://linkedin.com/in/yourprofile
  github:
    personal: https://github.com/yourhandle
    work: https://github.com/companyprofile

summary: >
  A brief paragraph about you — your focus, experience, values, and goals.

skills:
  programming_languages:
    - Python
    - Go
    - JavaScript
  cloud_and_data_platforms:
    - AWS (Lambda, EC2)
    - PostgreSQL
    - Redis

experience:
  - company: Example Corp
    role: Backend Engineer
    location: Remote
    start_date: Jan 2021
    end_date: Present
    bullets:
      - Built and maintained API services in Go
      - Integrated third-party APIs for payment and identity

education:
  - degree: B.Tech in Computer Science
    university: Your University
    period: Aug 2015 – May 2019
    location: City, Country

projects:
  - name: My Side Project
    description: >
      A short explanation of the goal or result of the project
    bullets:
      - Used FastAPI and SQLite to build the backend
      - Deployed on Fly.io

interests:
  - Photography
  - Writing blog posts
  - Contributing to open source

achievements:
  - Hackathon winner 2021 at XYZ event
```

---

## 🛠️ Extend This Project

Want to contribute? Here are great ways to take it forward:

### Support More Formats
- [ ] ✅ Input: JSON, TOML, Markdown
- [ ] ✅ Output: DOCX, PDF

### Support Themes
- [ ] Custom HTML/CSS templates
- [ ] Dark mode

### Add CLI Tooling

```bash
yaml2resume --input my.yaml --output resume.pdf
```

---

## Call for Contributions

If you're a developer or designer who loves clean documents and building personal tools — I'd love for you to contribute.

- Add themes or export formats
- Improve accessibility
- Build a simple web frontend
- Integrate support for DOCX, PDF, or JSON/YAML schema validators

---

## License

This project is licensed under the GNU GPL v3.0.

You're free to use, modify, distribute, and even use it commercially — but any derivative works must also remain open source and licensed under GPL v3.0, with proper attribution.
