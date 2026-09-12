import subprocess
from pathlib import Path

NOTEBOOK = "online_retail_analysis.ipynb"
HTML_FILE = Path("online_retail_analysis.html")

# Export notebook to HTML
subprocess.run(
    ["jupyter", "nbconvert", "--to", "html", NOTEBOOK],
    check=True
)

toc_code = """
<style>
#custom-toc {
    position: fixed;
    top: 20px;
    left: 20px;
    width: 280px;
    max-height: 90vh;
    overflow-y: auto;
    padding: 16px;
    background: white;
    border: 1px solid #ddd;
    border-radius: 8px;
    font-size: 14px;
    z-index: 9999;
}

#custom-toc ul {
    list-style: none;
    padding-left: 12px;
}

#custom-toc a {
    text-decoration: none;
}

#custom-toc .level-2 {
    padding-left: 12px;
}

#custom-toc .level-3 {
    padding-left: 24px;
}

body {
    margin-left: 330px !important;
}
</style>

<script>
document.addEventListener("DOMContentLoaded", function () {
    const toc = document.createElement("nav");
    toc.id = "custom-toc";

    const title = document.createElement("h3");
    title.textContent = "Table of Contents";
    toc.appendChild(title);

    const list = document.createElement("ul");

    document.querySelectorAll("h1, h2, h3").forEach((heading, index) => {
    const headingText = heading.textContent.replace("¶", "").trim();

    if (headingText === "Table of Contents") {
        return;
    }

    if (!heading.id) {
        heading.id = "section-" + index;
    }

    const item = document.createElement("li");
    item.className = "level-" + heading.tagName.substring(1);

    const link = document.createElement("a");
    link.href = "#" + heading.id;
    link.textContent = headingText;

    item.appendChild(link);
    list.appendChild(item);
});

    toc.appendChild(list);
    document.body.appendChild(toc);
});
</script>
"""

html = HTML_FILE.read_text(encoding="utf-8")
html = html.replace("</body>", toc_code + "\n</body>")
HTML_FILE.write_text(html, encoding="utf-8")

print("HTML created successfully with interactive Table of Contents.")