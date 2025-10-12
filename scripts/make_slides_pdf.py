from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import landscape, A4
from reportlab.lib.units import mm
import os
import re

INPUT = os.path.join('deliverables', 'slides_template.md')
OUTPUT = os.path.join('deliverables', 'slides.pdf')

def parse_slides(md_text):
    # Split on top-level headings (# ) into slides
    slides = []
    current = None
    for line in md_text.splitlines():
        m = re.match(r'^#\s+(.*)', line)
        if m:
            if current is not None:
                slides.append(current)
            current = {'title': m.group(1).strip(), 'body': []}
        else:
            if current is None:
                continue
            current['body'].append(line)
    if current is not None:
        slides.append(current)
    return slides

def render_slides(slides, output_path):
    c = canvas.Canvas(output_path, pagesize=landscape(A4))
    width, height = landscape(A4)
    left = 20 * mm
    top = height - 20 * mm
    c.setFont('Helvetica-Bold', 28)
    for s in slides:
        c.setFont('Helvetica-Bold', 28)
        c.drawCentredString(width / 2, top, s['title'])
        c.setFont('Helvetica', 14)
        y = top - 20 * mm
        for line in s['body']:
            if y < 20 * mm:
                c.showPage()
                c.setFont('Helvetica', 14)
                y = top - 20 * mm
            # simple wrap at 100 chars
            for chunk in [line[i:i+100] for i in range(0, len(line), 100)]:
                c.drawString(left, y, chunk)
                y -= 12
        c.showPage()
    c.save()


if __name__ == '__main__':
    if not os.path.exists(INPUT):
        print('Slides template not found:', INPUT)
    else:
        with open(INPUT, 'r', encoding='utf-8') as f:
            md = f.read()
        slides = parse_slides(md)
        if not slides:
            print('No slides found in template')
        else:
            os.makedirs(os.path.dirname(OUTPUT), exist_ok=True)
            render_slides(slides, OUTPUT)
            print('Wrote slides PDF:', OUTPUT)
