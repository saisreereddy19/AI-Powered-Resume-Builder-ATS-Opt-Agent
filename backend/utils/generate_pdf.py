from reportlab.lib.pagesizes import LETTER
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch

def build_pdf(data, out_path):
    c = canvas.Canvas(out_path, pagesize=LETTER)
    width, height = LETTER

    y = height - 1 * inch

    c.setFont("Helvetica-Bold", 18)
    c.drawString(1*inch, y, data["name"])
    y -= 0.4*inch

    c.setFont("Helvetica", 12)
    c.drawString(1*inch, y, data["email"])
    y -= 0.2*inch
    c.drawString(1*inch, y, data["phone"])
    y -= 0.4*inch

    c.setFont("Helvetica-Bold", 14)
    c.drawString(1*inch, y, "Experience")
    y -= 0.3*inch

    c.setFont("Helvetica", 12)
    for exp in data["experience"]:
        for line in exp.split("\n"):
            c.drawString(1*inch, y, line)
            y -= 0.2*inch
            if y < 1*inch:
                c.showPage()
                y = height - 1*inch
                c.setFont("Helvetica", 12)

    c.save()
