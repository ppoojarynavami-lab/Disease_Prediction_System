from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

def create_pdf(disease, diet, avoid, routine):

    pdf = SimpleDocTemplate("Health_Report.pdf")

    styles = getSampleStyleSheet()

    elements = []

    title = Paragraph(
        "<b>AI Healthcare Report</b>",
        styles['Title']
    )

    elements.append(title)

    elements.append(Spacer(1, 20))

    disease_text = Paragraph(
        f"<b>Disease Prediction:</b> {disease}",
        styles['BodyText']
    )

    elements.append(disease_text)

    elements.append(Spacer(1, 10))

    diet_text = Paragraph(
        f"<b>Recommended Diet:</b> {', '.join(diet)}",
        styles['BodyText']
    )

    elements.append(diet_text)

    elements.append(Spacer(1, 10))

    avoid_text = Paragraph(
        f"<b>Foods To Avoid:</b> {', '.join(avoid)}",
        styles['BodyText']
    )

    elements.append(avoid_text)

    elements.append(Spacer(1, 10))

    routine_text = Paragraph(
        f"<b>Daily Routine:</b> {', '.join(routine)}",
        styles['BodyText']
    )

    elements.append(routine_text)

    pdf.build(elements)