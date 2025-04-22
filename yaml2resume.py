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
    @page { size: A4; margin: 19mm; }
    body { font-family: 'Open Sans', sans-serif; font-size: 10.5pt; color: #222; line-height: 1.6; }
    .resume-container { max-width: 720px; margin: auto; padding: 16px; }
    .section { margin-top: 36px; padding-top: 10px; border-top: 1px solid #ccc; }
    h1 { font-size: 22pt; font-weight: bold; margin-bottom: 5px; }
    h2 { font-size: 13pt; color: #333; margin-top: 20px; }
    h3 { font-size: 11.5pt; font-weight: bold; margin-top: 12px; }
    ul { margin-left: 20px; }
    a { color: #00449e; text-decoration: none; }
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

    <div class="section"><h2>Skills</h2>
        {"".join(f"<h3>{k.replace('_',' ').title()}</h3><p>{', '.join(v)}</p>" for k, v in resume['skills'].items())}
    </div>

    <div class="section"><h2>Work Experience</h2>
        {"".join(
            f"<div><h3>{j['role']}</h3><p><strong>{j.get('display_name', j['company'])}</strong> | {j['start_date']} – {j['end_date']} | {j['location']}</p><ul>{''.join(f'<li>{b}</li>' for b in j['bullets'])}</ul></div>"
            for j in resume['experience'])}
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
    input_path = "sample/sample.yaml"
    output_path = "sample/sample.html"
    generate_resume_html(input_path, output_path)

if __name__ == "__main__":
    main()