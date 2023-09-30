import csv
from fpdf import FPDF
from fpdf.fonts import FontFace

with open("countries.txt", encoding="utf8") as csv_file:
    data = list(csv.reader(csv_file, delimiter=","))

pdf = FPDF()
pdf.set_font("helvetica", size=14)

pdf.add_page()
with pdf.table() as table:
    for data_row in data:
        row = table.row()

        for datum in data_row:
            row.cell(datum)

pdf.add_page()
pdf.set_draw_color(255, 0, 0)
pdf.set_line_width(0.3)
headings_style = FontFace(emphasis="BOLD", color=255, fill_color=(255, 100, 0))
with pdf.table(
        borders_layout="NO_HORIZONTAL_LINES",
        cell_fill_color=(224, 235, 255),
        # cell_fill_mode=lambda i, j: i % 2,
        col_widths=(42, 39, 35, 42),
        headings_style=headings_style,
        line_height=6,
        text_align=("LEFT", "CENTER", "RIGHT", "RIGHT"),
        width=160,
) as table:
    for data_row in data:
        row = table.row()
        for datum in data_row:
            row.cell(datum)

pdf.output("tuto5.pdf")

Lecture: Adding
Links & HTML
To
PDF
Page.
from fpdf import FPDF

pdf = FPDF()

pdf.add_page()
pdf.set_font("helvetica", size=20)
pdf.write(5, "To find out what's new in self tutorial, click ")
pdf.set_font(style="U")
link = pdf.add_link(page=2)
pdf.write(5, "here", link)
pdf.set_font()

pdf.add_page()
pdf.image(
    "demo.png", 10, 10, 50, 0, "", "<https://www.google.com>"
)
pdf.set_left_margin(60)
pdf.set_font_size(18)
pdf.write_html(
    """You can print text mixing different styles using HTML tags: <b>bold</b>, <i>italic</i>,
<u>underlined</u>, or <b><i><u>all at once</u></i></b>!
<br><br>You can also insert links on text, such as <a href="<https://www.google.com>"><https://www.google.com></a>,
or on an image: the logo is clickable!"""
)
pdf.output("tuto6.pdf")
