from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch

def generate_altacv_pdf(data, filename):
    c = canvas.Canvas(filename, pagesize=letter)
    width, height = letter

    y = height - 50

    c.setFont("Helvetica-Bold", 20)
    c.drawString(50, y, data["personal_info"]["full_name"])
    y -= 30

    c.setFont("Helvetica", 12)
    c.drawString(50, y, f"{data['personal_info']['email']} | {data['personal_info']['phone']}")
    y -= 40

    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, y, "Skills")
    y -= 20
    c.setFont("Helvetica", 12)
    for s in data["skills"]:
        c.drawString(60, y, f"• {s}")
        y -= 15

    y -= 20
    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, y, "Experience")
    y -= 20
    c.setFont("Helvetica", 12)

    for exp in data["experience"]:
        c.drawString(50, y, f"{exp['role']} — {exp['company']}")
        y -= 15
        c.drawString(60, y, exp["description"])
        y -= 25

    c.save()
