import io
import os
import datetime
import json
import sys
from reportlab.lib import colors
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.platypus import Image, Paragraph, Spacer, SimpleDocTemplate, Table, TableStyle, LongTable, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle as PS
from reportlab.platypus.flowables import TopPadder
from  reportlab.platypus.tableofcontents import TableOfContents
from  reportlab.lib.units import cm, mm, inch

class PageNumCanvas(canvas.Canvas):

    def __init__(self, *args, **kwargs):

        canvas.Canvas.__init__(self, *args, **kwargs)
        self.pages = []

    def showPage(self):

        self.pages.append(dict(self.__dict__))
        self._startPage()

    def save(self):

        page_count = len(self.pages)

        for page in self.pages:
            self.__dict__.update(page)
            self.draw_page_number(page_count)
            canvas.Canvas.showPage(self)

        canvas.Canvas.save(self)

    def draw_page_number(self, page_count):

        page = "Page %s of %s" % (self._pageNumber, page_count)
        self.setFont("Helvetica", 10)
        self.drawRightString(195 * mm, 10 * mm, page)

class MyDocTemplate(SimpleDocTemplate):
    def __init__(self, filename, **kw):
        self.allowSplitting = 0
        apply(SimpleDocTemplate.__init__, (self, filename), kw)

    def afterFlowable(self, flowable):
        "Registers TOC entries."
        if flowable.__class__.__name__ == 'Paragraph':
            text = flowable.getPlainText()
            style = flowable.style.name
            if style == 'Heading1':
                self.notify('TOCEntry', (0, text, self.page))
            if style == 'Heading2':
                self.notify('TOCEntry', (1, text, self.page))

def generate_report(data):

    ip = str(data['camInfo']['ip'])
    port = str(data['camInfo']['port'])
    cam = 'Device under Test: ' + ip + ':' + port
    test_time = 'Report generated: ' + str(datetime.datetime.now())
    testsResults = data['runnedTests']
    img_url = '.' + data['camInfo']['snapshot_url']
    url = 'reports/' + ip + ':' + port + '.' + str(datetime.datetime.now().time()) + '.pdf'

    styles = getSampleStyleSheet()
    centered = PS(name = 'centered',
        fontSize = 14,
        leading = 16,
        alignment = 1,
        spaceAfter = 10)

    h1 = PS(
        name = 'Heading1',
        fontSize = 12,
        leading = 14)


    bold = PS(
        name = 'bold',
        fontName='Helvetica-Bold',
        fontSize=14,
        leading=16 )

    centered_bold = PS(name = 'centered_bold',
        fontSize = 14,
        fontName='Helvetica-Bold',
        leading = 16,
        alignment = 1,
        spaceAfter = 10)


    h2 = PS(name = 'Heading2',
        fontSize = 10,
        leading = 12)

    Report = []

    Report.append(Paragraph('ONVIF COMPLIANCE TESTER', centered_bold))
    Report.append(Spacer(1, 12))
    Report.append(Spacer(1, 12))
    im = Image(img_url, 5 * inch, 3 * inch)
    Report.append(im)
    Report.append(Spacer(1, 12))
    Report.append(Spacer(1, 12))
    Report.append(Paragraph('REPORT DATASHEET', centered_bold))
    Report.append(Spacer(1, 12))
    Report.append(Spacer(1, 12))
    Report.append(Paragraph(cam, centered))
    Report.append(Paragraph('Class: video_encoder, ptz, audio_encoder', centered))
    Report.append(Paragraph(test_time, centered))
    Report.append(Spacer(1, 12))
    Report.append(Spacer(1, 12))
    Report.append(Spacer(1, 12))
    logo = Image(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'logo.png'))
    Report.append(TopPadder(logo))
    Report.append(PageBreak())

    Report.append(Paragraph('<b>Table of contents</b>', centered))

    toc = TableOfContents()
    toc.levelStyles = [
        PS(fontName='Times-Bold', fontSize=14, name='TOCHeading1', leftIndent=20, firstLineIndent=-20, spaceBefore=10, leading=16),
        PS(fontSize=12, name='TOCHeading2', leftIndent=40, firstLineIndent=-20, spaceBefore=5, leading=12),
    ]
    Report.append(toc)
    Report.append(PageBreak())

    styleN = styles['Normal']
    styleN.wordWrap = 'CJK'

    def doHeading(text, sty):
        from hashlib import sha1
        bn = sha1(text + sty.name).hexdigest()
        h = Paragraph(text + '<a name="%s"/>' % bn, sty)
        h._bookmarkName = bn
        Report.append(h)

    for item in testsResults.keys():

        doHeading('{} Service Features'.format(item.capitalize()), h2)
        Report.append(Spacer(1, 12))

        data = []
        data.append(['Features', 'Description'])

        for response in testsResults[item]:
            if response['data']['result']['supported'] == False:
                report = 'Not Supported'
            else:
                try:
                    response['data']['result']['report']
                    report = response['data']['result']['report']
                except:
                    report = 'Supported'

            data.append([response['data']['name'], report])

        data_proccessed = [[Paragraph(cell, styleN) for cell in row] for row in data]

        table = LongTable(data_proccessed, colWidths=['30%', '70%'])
        table.setStyle(TableStyle([('BOX',(0,0),(-1,-1),1,colors.black),
                            ('GRID',(0,0),(-1,-1),0.5,colors.black),
                            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
                            ('BACKGROUND', (0, 0), (-1, 0), colors.gray),
                            ('ALIGN', (0, 0), (-1, -0), 'CENTER')]))
        Report.append(table)
        Report.append(Spacer(1, 12))

    # story.append(PageBreak())

    # ptext = "<font size=16>%s</font>" % cam

    # Report.append(Paragraph(ptext, styles["Normal"]))
    # Report.append(Spacer(1, 12))
    # Report.append(Paragraph("<font size=12>%s</font>" % test_time, styles["Normal"]))
    # Report.append(Spacer(1, 12))

    # for counter, item in enumerate(testsResults, 1):
    #     if item["data"]["name"]:
    #         ptext = str(counter) +  ".Test:  " + str(item["data"]["name"]) + "(" + str(item["data"]["service"]) + ")"
    #     else:
    #         ptext = "Test: " + "NameError"
    #     if item["data"]["result"]["supported"]:
    #         flag = item["data"]["result"]["supported"]
    #         if (flag == False):
    #             sutext = str(item["data"]["name"] + ' is not supported')
    #         else:
    #             sutext = str(item["data"]["name"] + ' is supported')
    #     else:
    #         sutext = None
    #     if item["data"]["result"]["response"]:
    #         rtext = "Response: " + str(json.dumps(item["data"]["result"]["response"], sort_keys=True, indent=4))
    #     else:
    #         rtext = "Response: " + "None"
    #     if item["data"]["result"]["extension"]:
    #         etext = "Test Feature: " + str(item["data"]["result"]["extension"])
    #     else:
    #         etext = "Test Feature: " + "None"
    #     Report.append(Paragraph("<font size=14>%s</font>" % ptext, styles["Heading5"]))
    #     Report.append(Spacer(1, 8))
    #     if (sutext is not None):
    #         Report.append(Paragraph(sutext, styles["Normal"], bulletText=u'\u25cf'))
    #         Report.append(Spacer(1, 8))
    #     if ((etext != None)):
    #         Report.append(Paragraph(etext, styles["Normal"], bulletText=u'\u25cf'))
    #         Report.append(Spacer(1, 8))
    #     if ((item["data"]["result"]["response"]) or (len(item["data"]["result"]["response"]) != 0)):
    #         Report.append(Paragraph(rtext, styles["Normal"], bulletText=u'\u25cf'))
    #         Report.append(Spacer(1, 8))
    #     Report.append(Spacer(1, 12))

    doc = MyDocTemplate(url, pagesize=A4, rightMargin=15*mm, leftMargin=15*mm, topMargin=15*mm, bottomMargin=15*mm)
    doc.multiBuild(Report, canvasmaker=PageNumCanvas)

    return url
