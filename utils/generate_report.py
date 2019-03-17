import io
import datetime
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.platypus.tables import Table, TableStyle

 
def generate_report(data):

    Report = []
    ip = str(data['camInfo']['ip'])
    port = str(data['camInfo']['port'])
    testsResults = data['runnedTests']
    img_url = '.' + data['camInfo']['snapshot_url']
    url = './reports/' + ip + ':' + port + '.' + str(datetime.datetime.now().time()) + '.pdf'

    doc = SimpleDocTemplate(url, pagesize=A4,
                        rightMargin=20, leftMargin=20,
                        topMargin=20, bottomMargin=20)

    im = Image(img_url, 12.7 * cm, 9.525 * cm)
    Report.append(im)

    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))
    ptext = '<font size=14>%s</font>' % ip

    Report.append(Paragraph(ptext, styles["Normal"]))
    Report.append(Spacer(1, 12))

    for counter, item in enumerate(testsResults, 1):
        ptext = 'Test: ' + str(item["data"]["name"])
        rtext = 'Response: ' + str(item["data"]["result"]["response"])
        etext = item["data"]["result"]["extension"]
        Report.append(Paragraph(ptext, styles["Normal"]))
        Report.append(Spacer(1, 12))
        if ((etext != None)):
            Report.append(Paragraph(etext, styles["Normal"]))
            Report.append(Spacer(1, 12))
        if ((item["data"]["result"]["response"]) or (len(item["data"]["result"]["response"]) != 0)):
            Report.append(Paragraph(rtext, styles["Normal"]))
            Report.append(Spacer(1, 12))
        Report.append(Paragraph("<--------------------->", styles["Normal"]))
        Report.append(Spacer(1, 12))
        # row1 = ("number", ptext)
        # row2 = ("", rtext)
        # data.append(row1)
        # data.append(row2)

    # table = Table(data, hAlign='LEFT', colWidths=200)
    # table.setStyle(TableStyle([
    #         ('ALIGN', (10, 0), (-1, 0), 'CENTER'),
    #         ('ALIGN', (0, 0), (0, -1), 'LEFT'),
    #         ('INNERGRID', (0, 0), (-1, -1), 0.50, colors.black),
    #         ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
    #     ]))
    # Report.append(table)
    doc.build(Report)
