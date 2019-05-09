import io
import datetime
import json
import sys
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
    test_time = 'Test time: ' + str(datetime.datetime.now())
    cam = 'Device: ' + ip + ':' + port
    testsResults = data['runnedTests']
    print testsResults
    img_url = '.' + data['camInfo']['snapshot_url']
    url = 'reports/' + ip + ':' + port + '.' + str(datetime.datetime.now().time()) + '.pdf'

    doc = SimpleDocTemplate(url, pagesize=A4,
                        rightMargin=20, leftMargin=20,
                        topMargin=20, bottomMargin=20)

    im = Image(img_url, 12.7 * cm, 9.525 * cm)
    Report.append(im)

    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name= "Justify ", alignment=TA_JUSTIFY))

    Report.append(Paragraph(testsResults, styles["Normal"]))
    Report.append(Spacer(1, 12))

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

    doc.build(Report)
    return url
