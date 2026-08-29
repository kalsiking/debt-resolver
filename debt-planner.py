import os
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

def create_tracker():
    os.makedirs('generated', exist_ok=True)
    pdf_path = "generated/debt_payoff_tracker.pdf"
    doc = SimpleDocTemplate(pdf_path, pagesize=letter, rightMargin=54, leftMargin=54, topMargin=54, bottomMargin=54, title="3-Month Debt Payoff Tracker")
    story = []
    
    styles = getSampleStyleSheet()
    title_style = ParagraphStyle('TitleStyle', parent=styles['Heading1'], fontSize=24, leading=28, textColor=colors.HexColor("#1A365D"), spaceAfter=12)
    subtitle_style = ParagraphStyle('SubTitleStyle', parent=styles['Normal'], fontSize=11, leading=15, textColor=colors.HexColor("#4A5568"), spaceAfter=20)
    section_style = ParagraphStyle('SectionStyle', parent=styles['Heading2'], fontSize=14, leading=18, textColor=colors.HexColor("#2B6CB0"), spaceBefore=15, spaceAfter=8)
    body_style = ParagraphStyle('BodyStyle', parent=styles['Normal'], fontSize=10, leading=14, textColor=colors.HexColor("#2D3748"))
    
    # Title & Intro
    story.append(Paragraph("<b>Gemini 3-Month Debt Payoff Tracker</b>", title_style))
    story.append(Paragraph("A structured visual ledger to map your liabilities, track monthly progress, and reclaim your financial cash flow between September and November 2026.", subtitle_style))
    story.append(Spacer(1, 10))
    
    # Section 1: Master Inventory
    story.append(Paragraph("<b>1. Debt Inventory Ledger</b>", section_style))
    headers = ["Debt Name / Creditor", "Total Balance", "Interest Rate (APR)", "Minimum Payment", "Target Order"]
    data = [headers]
    for _ in range(5):
        data.append(["", "", "", "", ""])
        
    t1 = Table(data, colWidths=[150, 90, 100, 100, 64], rowHeights=[24]+[30]*5)
    t1.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#F7FAFC")),
        ('TEXTCOLOR', (0,0), (-1,0), colors.HexColor("#2D3748")),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,0), 9),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#CBD5E0")),
    ]))
    story.append(t1)
    story.append(Spacer(1, 15))
    
    # Section 2: 3-Month Progress Tracker
    story.append(Paragraph("<b>2. 3-Month Milestone Ledger</b>", section_style))
    headers_m = ["Target Debt Name", "September Payment", "October Payment", "November Payment", "Current Status"]
    data_m = [headers_m]
    for _ in range(4):
        data_m.append(["", "", "", "", "[  ] Cleared!"])
        
    t2 = Table(data_m, colWidths=[130, 95, 95, 95, 89], rowHeights=[24]+[30]*4)
    t2.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#F7FAFC")),
        ('TEXTCOLOR', (0,0), (-1,0), colors.HexColor("#2D3748")),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,0), 9),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#CBD5E0")),
    ]))
    story.append(t2)
    story.append(Spacer(1, 20))
    
    # Strategy Reminder Box
    story.append(Paragraph("<b>💡 Execution Reminders:</b>", body_style))
    story.append(Paragraph("• <b>Snowball Velocity:</b> As soon as a debt is completely cleared, roll its entire monthly payment amount directly into your next priority target.", body_style))
    story.append(Paragraph("• <b>Automation Guardrail:</b> Keep all baseline minimum payments entirely on auto-pay to eliminate the risk of late fees or credit dings.", body_style))
    
    doc.build(story)

create_tracker()
