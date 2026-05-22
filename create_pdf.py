#!/usr/bin/env python3
"""Create print-ready PDF for Stephen's New Friends"""

import os
import sys
from reportlab.lib.pagesizes import letter, landscape, portrait
from reportlab.lib.units import inch
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.colors import HexColor, black
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, PageBreak
from reportlab.lib.enums import TA_CENTER, TA_LEFT

# Book dimensions: 8.5" x 8.5" square
PAGE_WIDTH = 8.5 * inch
PAGE_HEIGHT = 8.5 * inch
MARGIN = 0.5 * inch
CONTENT_WIDTH = PAGE_WIDTH - (2 * MARGIN)

# Colors
CREAM = HexColor("#FFFEF7")
CHARCOAL = HexColor("#333333")
CORAL = HexColor("#F1948A")
YELLOW = HexColor("#F4D03F")
GREEN = HexColor("#82E0AA")
BLUE = HexColor("#85C1E9")

output_path = "/Users/jarvis/.openclaw/workspace/rj-books/Stephens_New_Friends.pdf"

# Create document
doc = SimpleDocTemplate(
    output_path,
    pagesize=portrait((PAGE_WIDTH, PAGE_HEIGHT)),
    leftMargin=MARGIN,
    rightMargin=MARGIN,
    topMargin=MARGIN,
    bottomMargin=MARGIN
)

styles = getSampleStyleSheet()

# Custom styles
title_style = ParagraphStyle(
    'BookTitle',
    parent=styles['Title'],
    fontSize=48,
    textColor=CHARCOAL,
    alignment=TA_CENTER,
    spaceAfter=20,
    fontName='Helvetica-Bold'
)

subtitle_style = ParagraphStyle(
    'BookSubtitle',
    parent=styles['Normal'],
    fontSize=18,
    textColor=CHARCOAL,
    alignment=TA_CENTER,
    spaceAfter=40,
    fontName='Helvetica'
)

author_style = ParagraphStyle(
    'BookAuthor',
    parent=styles['Normal'],
    fontSize=16,
    textColor=CORAL,
    alignment=TA_CENTER,
    spaceAfter=30,
    fontName='Helvetica-Bold'
)

text_style = ParagraphStyle(
    'BookText',
    parent=styles['Normal'],
    fontSize=20,
    textColor=CHARCOAL,
    alignment=TA_CENTER,
    spaceAfter=15,
    spaceBefore=15,
    fontName='Helvetica',
    leading=28
)

heading_style = ParagraphStyle(
    'BookHeading',
    parent=styles['Heading2'],
    fontSize=24,
    textColor=CORAL,
    alignment=TA_CENTER,
    spaceAfter=20,
    fontName='Helvetica-Bold'
)

page_num_style = ParagraphStyle(
    'PageNum',
    parent=styles['Normal'],
    fontSize=10,
    textColor=CHARCOAL,
    alignment=TA_CENTER,
    fontName='Helvetica'
)

# Build content
story = []

# === COVER PAGE ===
story.append(Spacer(1, 1.5*inch))
story.append(Paragraph("Stephen's New Friends", title_style))
story.append(Spacer(1, 0.3*inch))
story.append(Paragraph("An RJ-Books Story", subtitle_style))
story.append(Spacer(1, 0.5*inch))
story.append(Paragraph("By Ryan Lambiasi", author_style))
story.append(Spacer(1, 1*inch))

# Add cover image if it exists
cover_img = "/Users/jarvis/.openclaw/workspace/rj-books/illustrations/stephen-cover-concept---7d02effb-8956-4896-8aa4-0bbd93415c0d.png"
if os.path.exists(cover_img):
    img = Image(cover_img, width=4*inch, height=3*inch)
    story.append(img)

story.append(PageBreak())

# === TITLE PAGE ===
story.append(Spacer(1, 2*inch))
story.append(Paragraph("Stephen's New Friends", title_style))
story.append(Spacer(1, 0.3*inch))
story.append(Paragraph("An RJ-Books Story", subtitle_style))
story.append(Spacer(1, 0.5*inch))
story.append(Paragraph("By Ryan Lambiasi", author_style))
story.append(PageBreak())

# === COPYRIGHT PAGE ===
story.append(Spacer(1, 2*inch))
story.append(Paragraph("© 2026 RJ-Books", text_style))
story.append(Spacer(1, 0.3*inch))
story.append(Paragraph("All rights reserved.", text_style))
story.append(Spacer(1, 0.5*inch))
story.append(Paragraph("RJ-Books", text_style))
story.append(Paragraph("Stories for big feelings, little hearts.", subtitle_style))
story.append(PageBreak())

# === DEDICATION ===
story.append(Spacer(1, 3*inch))
story.append(Paragraph("For every child", text_style))
story.append(Paragraph("who has felt nervous", text_style))
story.append(Paragraph("about something new.", text_style))
story.append(PageBreak())

# === STORY PAGES ===
pages = [
    {
        "title": "Meet Stephen",
        "text": [
            "This is Stephen.",
            "He is four years old.",
            "",
            "Stephen lives in a white house",
            "with Mommy, Daddy,",
            "and Jackson."
        ],
        "image": "stephen-spread2-intro---cdb13b8b-3314-4d6a-a34a-7ebc82778c21.png"
    },
    {
        "title": "The Friends Across the Street",
        "text": [
            "Stephen loves the people",
            "who live across the street.",
            "",
            "They wave every morning.",
            "They smile every night."
        ],
        "image": "stephen-spread5-neighbors---c7a19ffe-b00f-4182-adbb-f2df89e12c3d.png"
    },
    {
        "title": "One Day...",
        "text": [
            "One day,",
            "Stephen does not see them.",
            "",
            "Their car is gone.",
            "Their lights are dark."
        ],
        "image": "stephen-spread7-empty---4332a712-1ef2-4516-9c9e-9df5d02c58c9.png"
    },
    {
        "title": "The Bad Day",
        "text": [
            "The next day,",
            "big machines come.",
            "",
            "CRASH! BANG!",
            "The house across the street",
            "comes down.",
            "",
            "Stephen cries."
        ],
        "image": "stephen-spread5-sad---9b7c18fd-80dc-4e7e-9969-6a07c5613897.png"
    },
    {
        "title": "Jackson Knows",
        "text": [
            "Jackson knows",
            "when Stephen is sad.",
            "",
            "Jackson leans close.",
            "Jackson licks the tears away.",
            "",
            "\"I love you,\"",
            "says Jackson."
        ],
        "image": "stephen-spread7-comfort---f587a6bb-18d8-4f17-8c61-60764298a1ae.png"
    },
    {
        "title": "Mommy and Daddy Help",
        "text": [
            "Mommy sits with Stephen.",
            "Daddy holds his hand.",
            "",
            "\"It is okay to be sad,\"",
            "they say.",
            "",
            "\"We are here.\""
        ],
        "image": "stephen-spread13-parents---05470dc4-ff88-4c6f-b6eb-c8cb6b4b4746.png"
    },
    {
        "title": "A Few Days Later",
        "text": [
            "A few days later,",
            "a cement mixer comes.",
            "",
            "VROOM!",
            "It pours a new floor.",
            "",
            "\"What is happening?\"",
            "asks Stephen."
        ],
        "image": "stephen-spread8-cement---ad54c70f-6d2c-431a-ad92-641ee3b657b4.png"
    },
    {
        "title": "Daddy's Promise",
        "text": [
            "Daddy smiles.",
            "",
            "\"A new house is coming,\"",
            "he says.",
            "",
            "\"And do you know what?",
            "New friends will live there!\""
        ],
        "image": "stephen-spread17-promise---c02eaffa-21c4-40df-9b02-b259c3a2c0be.png"
    },
    {
        "title": "Every Morning",
        "text": [
            "Every morning,",
            "Stephen sits outside.",
            "",
            "He watches the walls go up.",
            "He watches the roof grow.",
            "",
            "He waves to the workers."
        ],
        "image": "stephen-spread10-morning---b070728a-b447-4c35-980b-c89b58cd2d90.png"
    },
    {
        "title": "Breakfast with Jackson",
        "text": [
            "One special day,",
            "Stephen and Jackson",
            "eat breakfast outside.",
            "",
            "UP, UP, UP",
            "go the beams",
            "for the new roof!"
        ],
        "image": "stephen-spread21-breakfast---a03a6347-2e8e-42cd-9f6f-6d6d26c08d08.png"
    },
    {
        "title": "New Trees",
        "text": [
            "The workers plant trees.",
            "They plant flowers.",
            "",
            "Stephen helps.",
            "",
            "\"This will be a happy home,\"",
            "says Stephen."
        ],
        "image": "stephen-spread12-trees---dee8eb3e-1826-475a-a1bf-2e141a3ef785.png"
    },
    {
        "title": "Where Are They?",
        "text": [
            "One day,",
            "the workers do not come.",
            "",
            "Stephen waits.",
            "Stephen worries.",
            "",
            "\"Where is everyone?\""
        ],
        "image": "stephen-spread25-waiting---64875365-4ec2-4f08-9011-4c673039851d.png"
    },
    {
        "title": "The Moving Van",
        "text": [
            "A few days later,",
            "a BIG truck comes.",
            "",
            "Boxes come out.",
            "A new family is here!"
        ],
        "image": "stephen-spread14-moving---7ded8fd4-862b-42c8-9fd3-b04607df3359.png"
    },
    {
        "title": "Meet Nora",
        "text": [
            "A girl comes out.",
            "She is Stephen's age.",
            "",
            "Her name is Nora.",
            "She has a teddy bear."
        ],
        "image": "stephen-spread29-nora---606cad7e-6829-4ed0-8981-5dc4259d81ec.png"
    },
    {
        "title": "Nervous Stephen",
        "text": [
            "Stephen is nervous.",
            "His tummy feels funny.",
            "",
            "But Daddy holds his hand.",
            "Jackson walks first."
        ],
        "image": "stephen-spread16-hello---d43d8b2e-5d1b-4710-b127-0adbee6b90cf.png"
    },
    {
        "title": "Saying Hello",
        "text": [
            "\"Hello,\" says Stephen.",
            "He gives Nora a flower.",
            "",
            "\"Hello,\" says Nora.",
            "She gives him a smile."
        ],
        "image": "stephen-spread17-nora---51b53560-89ff-4aa1-a4ba-032fa47dfcc3.png"
    },
    {
        "title": "The Beginning",
        "text": [
            "Stephen and Nora are friends.",
            "",
            "They play every day.",
            "",
            "Sometimes change is scary.",
            "But sometimes...",
            "it brings new friends."
        ],
        "image": "stephen-spread18-happy---0dfa4607-cc42-415d-8da9-d9dba2f908b3.png"
    }
]

# Build each page
for i, page in enumerate(pages):
    # Add page heading
    story.append(Spacer(1, 0.2*inch))
    story.append(Paragraph(page["title"], heading_style))
    story.append(Spacer(1, 0.2*inch))
    
    # Add image
    img_path = f"/Users/jarvis/.openclaw/workspace/rj-books/illustrations/{page['image']}"
    if os.path.exists(img_path):
        img = Image(img_path, width=5.5*inch, height=4*inch)
        story.append(img)
    
    story.append(Spacer(1, 0.3*inch))
    
    # Add text
    for line in page["text"]:
        if line == "":
            story.append(Spacer(1, 0.2*inch))
        else:
            story.append(Paragraph(line, text_style))
    
    story.append(PageBreak())

# === BACK COVER ===
story.append(Spacer(1, 1.5*inch))
story.append(Paragraph("RJ-Books", title_style))
story.append(Spacer(1, 0.3*inch))
story.append(Paragraph("Stories for big feelings,", subtitle_style))
story.append(Paragraph("little hearts.", subtitle_style))
story.append(Spacer(1, 0.5*inch))
story.append(Paragraph("By Ryan Lambiasi", author_style))

# Add back cover image
back_img = "/Users/jarvis/.openclaw/workspace/rj-books/illustrations/stephen-back-cover---6d7b2654-a115-4983-a9da-9f944fed12d3.png"
if os.path.exists(back_img):
    story.append(Image(back_img, width=4*inch, height=3*inch))

# Build the PDF
doc.build(story)
print(f"PDF created successfully: {output_path}")
print(f"File size: {os.path.getsize(output_path) / 1024:.1f} KB")
