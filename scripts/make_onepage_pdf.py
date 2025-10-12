from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
import textwrap
import os

INPUT = os.path.join('deliverables', 'one_page_writeup.md')
OUTPUT = os.path.join('deliverables', 'one_page_writeup.pdf')

def md_to_pdf(input_path, output_path):
    with open(input_path, 'r', encoding='utf-8') as f:
        text = f.read()

    c = canvas.Canvas(output_path, pagesize=A4)
    width, height = A4
    left = 20 * mm
    right = 20 * mm
    usable_width = width - left - right
    max_chars = int(usable_width / (6.5))  # approx char width for 11pt

    y = height - 20 * mm
    c.setFont('Helvetica', 11)
    line_height = 13

    # Simple approach: preserve paragraphs and wrap lines
    paragraphs = text.split('\n\n')
    for para in paragraphs:
        # replace multiple newlines and strip
        para = para.replace('\n', ' ').strip()
        if not para:
            y -= line_height
            continue
        wrapped = textwrap.wrap(para, width=max_chars)
        for line in wrapped:
            if y < 20 * mm:
                c.showPage()
                c.setFont('Helvetica', 11)
                y = height - 20 * mm
            c.drawString(left, y, line)
            y -= line_height
        y -= line_height / 2

    c.save()


if __name__ == '__main__':
    if not os.path.exists(INPUT):
        print(f"Input file not found: {INPUT}")
    else:
        os.makedirs(os.path.dirname(OUTPUT), exist_ok=True)
        md_to_pdf(INPUT, OUTPUT)
        print(f"Wrote PDF: {OUTPUT}")
