import io
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus.tables import Table, TableStyle

#ToDo:
# import snapshot
# import data from API
# 
# def generate_report():
#     doc = SimpleDocTemplate("camera.pdf", pagesize=A4,
#                         rightMargin=20, leftMargin=20,
#                         topMargin=20, bottomMargin=20)
#     Report = []
#     logo = "cam.jpg"

#     testsResults = [
#     {
#     "response": {
#         "name": "GetServiceCapabilities",
#         "result": {
#         "extension": None,
#         "response": "(Capabilities){\n   _WSPullPointSupport = True\n   _MaxPullPoints = 10\n   _MaxNotificationProducers = 10\n   _WSPausableSubscriptionManagerInterfaceSupport = False\n   _WSSubscriptionPolicySupport = True\n }",
#         "supported": True
#         },
#         "service": "Events",
#         "test_id": 2
#     }
#     },
#     {
#     "response": {
#         "name": "GetVideoOutputs",
#         "result": {
#         "extension": "The DUT did not send GetVideoOutputsResponse message",
#         "response": "[]",
#         "supported": False
#         },
#         "service": "deviceio",
#         "test_id": 7
#     }
#     },
#     {
#     "response": {
#         "name": "GetServiceCapabilities",
#         "result": {
#         "extension": None,
#         "response": "(Capabilities){\n   _AnalyticsModuleSupport = True\n   _RuleSupport = True\n   _CellBasedSceneDescriptionSupported = True\n }",
#         "supported": True
#         },
#         "service": "Analytics",
#         "test_id": 0
#     }
#     }
#     ]

#     im = Image(logo, 4 * inch, 2 * inch)
#     Report.append(im)

#     styles = getSampleStyleSheet()
#     styles.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))
#     ptext = '<font size=12>%s</font>' % '192.168.15.42:80'

#     Report.append(Paragraph(ptext, styles["Normal"]))
#     Report.append(Spacer(1, 12))

#     data = []
#     for counter, item in enumerate(testsResults, 1):
#         ptext = item["response"]["name"]
#         rtext = item["response"]["result"]["response"]
#         stext = item["response"]["service"]
#         Report.append(Paragraph(stext, styles["Normal"]))
#         Report.append(Spacer(1, 12))
#         row1 = ("number", ptext)
#         row2 = ("", rtext)
#         data.append(row1)
#         data.append(row2)

#     table = Table(data, hAlign='LEFT', colWidths=200)
#     table.setStyle(TableStyle([
#             ('ALIGN', (10, 0), (-1, 0), 'CENTER'),
#             ('ALIGN', (0, 0), (0, -1), 'LEFT'),
#             ('INNERGRID', (0, 0), (-1, -1), 0.50, colors.black),
#             ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
#         ]))
#     Report.append(table)
#     doc.build(Report)
