from pathlib import Path
from datetime import datetime

photos_dir = Path("photos")

# récupère tous les jpg
images = sorted(
    photos_dir.glob("*.jpg"),
    key=lambda p: p.stat().st_mtime
)

html_images = ""

for img in images:
    date = datetime.fromtimestamp(
        img.stat().st_mtime
    ).strftime("%d %B %Y")

    html_images += f"""
    <figure class="fade">
        <img src="{img.as_posix()}" alt="{img.stem}">
        <figcaption>{date}</figcaption>
    </figure>
    """

html = f"""
<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<meta name="viewport"
content="width=device-width, initial-scale=1.0">

<title>Galerie</title>

<style>

html {{
    scroll-behavior:smooth;
    scroll-snap-type:y mandatory;
}}

body {{
    margin:0;
    background:#0b0b0b;
    color:#ddd;
    font-family:Arial, sans-serif;
}}

.gallery {{
    display:flex;
    flex-direction:column;
    align-items:center;
}}

figure {{
    width:100%;
    min-height:100vh;

    display:flex;
    flex-direction:column;
    justify-content:center;
    align-items:center;

    scroll-snap-align:center;
}}

img {{
    width:min(92vw, 1200px);
    max-height:85vh;
    object-fit:contain;

    box-shadow:
        0 0 50px rgba(0,0,0,0.7);

    border-radius:4px;
}}

figcaption {{
    margin-top:1rem;
    opacity:0.5;
    font-size:0.9rem;
}}

</style>
</head>

<body>

<div class="gallery">
{html_images}
</div>

</body>
</html>
"""

Path("index.html").write_text(
    html,
    encoding="utf-8"
)

print("Galerie générée.")
