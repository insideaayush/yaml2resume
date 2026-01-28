import yaml
from pathlib import Path
import argparse
from jinja2 import Environment, FileSystemLoader
import markdown_it

md = markdown_it.MarkdownIt()

def markdown_filter(text):
    return md.render(text)

def load_resume(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

def format_github_links(github_dict):
    if not github_dict:
        return ""
    return "<br>".join(
        f"<a href='{url}' target='_blank'>{url}</a>" for _, url in github_dict.items()
    )

def build_html(resume, theme):
    template_dir = Path("templates") / theme
    if not template_dir.is_dir():
        raise FileNotFoundError(f"Theme '{theme}' not found.")

    env = Environment(loader=FileSystemLoader(str(template_dir)))
    env.filters['markdown'] = markdown_filter
    template = env.get_template("resume.html")

    css_path = template_dir / "style.css"
    with open(css_path, "r", encoding="utf-8") as f:
        css = f.read()

    contact_items = []
    if 'contact' in resume:
        for key, value in resume['contact'].items():
            if key == 'github':
                continue
            
            item = {'key': key.replace('_', ' ').title(), 'value': value, 'is_link': False}
            if key == 'email':
                item['is_link'] = True
                item['url'] = f"mailto:{value}"
            elif 'linkedin' in key:
                item['is_link'] = True
                item['url'] = value
            elif 'telegram' in key:
                item['is_link'] = True
                item['url'] = f"https://t.me/{value.replace('@', '')}"
            elif 'website' in key:
                item['is_link'] = True
                item['url'] = f"https://{value}"

            contact_items.append(item)

    half_len = (len(contact_items) + 1) // 2
    contact_col1 = contact_items[:half_len]
    contact_col2 = contact_items[half_len:]

    github_links = format_github_links(resume.get("contact", {}).get("github"))

    return template.render(
        resume=resume,
        css=css,
        github_links=github_links,
        contact_col1=contact_col1,
        contact_col2=contact_col2
    )

def generate_resume_html(input_path: str, output_path: str, theme: str) -> None:
    """
    Loads a resume YAML file and generates an ATS-friendly HTML file.

    Args:
        input_path (str): Path to the YAML resume file.
        output_path (str): Path to save the generated HTML file.
        theme (str): The theme to use for the resume.
    """
    resume = load_resume(input_path)
    html = build_html(resume, theme)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"✅ Resume generated with theme '{theme}': {output_path}")

def main():
    parser = argparse.ArgumentParser(description="Generate an HTML resume from a YAML file.")
    parser.add_argument(
        "-i", "--input",
        default="sample/resume_aayush_gautam_ATS_fixed.yaml",
        help="Path to the input YAML resume file."
    )
    parser.add_argument(
        "-o", "--output",
        default="sample/aayush_gautam_resume.html",
        help="Path to the output HTML file."
    )
    parser.add_argument(
        "-t", "--theme",
        default="default",
        help="The theme to use for the resume."
    )
    args = parser.parse_args()

    generate_resume_html(args.input, args.output, args.theme)

if __name__ == "__main__":
    main()