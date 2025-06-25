import os

# MathJaxスクリプト（先頭に挿入される）
MATHJAX_SCRIPT = """<script type="text/javascript"
  id="MathJax-script"
  async
  src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js">
</script>\n\n"""

def inject_to_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    if 'MathJax-script' in content:
        print(f"✔ 既に挿入済み: {filepath}")
        return

    if content.lstrip().startswith('---'):
        parts = content.split('---', 2)
        if len(parts) >= 3:
            header, rest = parts[1], parts[2]
            new_content = f"---{header}---\n\n{MATHJAX_SCRIPT}{rest.lstrip()}"
        else:
            new_content = f"{MATHJAX_SCRIPT}{content}"
    else:
        new_content = f"{MATHJAX_SCRIPT}{content}"

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"✅ 追加完了: {filepath}")

def process_directory(base_dir):
    for root, _, files in os.walk(base_dir):
        for name in files:
            if name.endswith('.md'):
                full_path = os.path.join(root, name)
                inject_to_file(full_path)

if __name__ == "__main__":
    process_directory("theory")
