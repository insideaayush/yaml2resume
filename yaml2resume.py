import yaml
from pathlib import Path

def load_resume(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

def format_github_links(github_dict):
    return "<br>".join(
        f"<a href='{url}' target='_blank'>{url}</a>" for _, url in github_dict.items()
    )

def build_html(resume):
    github_links = format_github_links(resume["contact"]["github"])

    css = """
<style>
    @page {
      size: A4;
      margin: 20mm;
    }
    body {
      font-family: 'Inter', 'Segoe UI', 'Open Sans', sans-serif;
      font-size: 11pt;
      color: #111;
      line-height: 1.6;
      background-color: #fff;
    }
    .resume-container {
      max-width: 800px;
      margin: auto;
      padding: 0 20px;
    }
    h1 {
      font-size: 28pt;
      font-weight: 700;
      margin-bottom: 5px;
      color: #000;
      border-bottom: 3px solid #000;
      padding-bottom: 6px;
    }
    h2 {
      font-size: 16pt;
      font-weight: 700;
      color: #000;
      margin-top: 36px;
      border-bottom: 1px solid #000;
      padding-bottom: 4px;
    }
    h3 {
      font-size: 13pt;
      font-weight: 700;
      color: #000;
      margin-top: 16px;
    }
    p {
      margin: 4px 0;
    }
    ul {
      margin: 6px 0 12px 20px;
      padding-left: 20px;
    }
    li {
      margin-bottom: 5px;
    }
    a {
      color: #000;
      text-decoration: none;
    }
    .contact p, .contact a {
      display: inline-block;
      margin-right: 12px;
    }
    .section {
      margin-top: 24px;
    }
    .print-note {
      font-size: 8pt;
      color: #888;
      text-align: center;
      margin-top: 20px;
    }
    @media print {
      a::after {
        content: " (" attr(href) ")";
        font-size: 9pt;
      }
      .print-note { display: none; }
    }
  </style>
    """

    html = f"""<!DOCTYPE html>
<html lang="en">
<head><meta charset="UTF-8"><title>{resume['name']} - Resume</title>{css}</head>
<body><div class="resume-container">
    <h1>{resume['name']}</h1>
    <p><strong>{resume['tagline']}</strong></p>
    <p>
        Email: <a href="mailto:{resume['contact']['email']}">{resume['contact']['email']}</a><br>
        Phone: {resume['contact']['phone']}<br>
        Location: {resume['contact']['location']}<br>
        LinkedIn: <a href="{resume['contact']['linkedin']}" target="_blank">{resume['contact']['linkedin']}</a><br>
        GitHub:<br>{github_links}
    </p>

    <div class="section"><h2>Summary</h2><p>{resume['summary']}</p></div>
    
    <div class="section"><h2>Work Experience</h2>
        {"".join(
            f"<div><h3>{j.get('display_name', j['company'])}</h3><p><strong>{j['role']}</strong> | {j['start_date']} – {j['end_date']} | {j['location']}</p><ul>{''.join(f'<li>{b}</li>' for b in j['bullets'])}</ul></div>"
            for j in resume['experience'])}
    </div>

    <div class="section"><h2>Skills</h2>
        {"".join(f"<h3>{k.replace('_',' ').title()}</h3><p>{', '.join(v)}</p>" for k, v in resume['skills'].items())}
    </div>

    <div class="section"><h2>Education</h2>
        {"".join(f"<p><strong>{e['degree']}</strong> | {e['university']} ({e['period']})<br>Location: {e['location']}</p>" for e in resume['education'])}
    </div>

    <div class="section"><h2>Projects</h2>
        {"".join(f"<div><h3>{p['name']}</h3><p>{p['description']}</p><ul>{''.join(f'<li>{b}</li>' for b in p['bullets'])}</ul></div>" for p in resume['projects'])}
    </div>

    <div class="section"><h2>Interests</h2><p>{', '.join(resume.get('interests', []))}</p></div>

    <div class="section"><h2>Achievements</h2>
        <ul>{"".join(f"<li>{a}</li>" for a in resume.get('achievements', []))}</ul>
    </div>
</div></body></html>"""

    return html

def generate_resume_html(input_path: str, output_path: str = "sample.html") -> None:
    """
    Loads a resume YAML file and generates an ATS-friendly HTML file.

    Args:
        input_path (str): Path to the YAML resume file.
        output_path (str): Path to save the generated HTML file (default: sample.html).
    """
    resume = load_resume(input_path)
    html = build_html(resume)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"✅ Resume generated: {output_path}")

def main():
    # Customize this if running standalone
    # input_path = "sample/sample.yaml"
    # output_path = "sample/sample.html"
    input_path = "sample/resume_aayush_gautam_ATS_fixed.yaml"
    output_path = "sample/aayush_gautam_resume.html"
    generate_resume_html(input_path, output_path)

if __name__ == "__main__":
    main()