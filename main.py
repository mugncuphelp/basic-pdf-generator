from fpdf import FPDF
import pandas as pd
from itertools import repeat

pdf = FPDF(orientation='P', unit='mm', format='A4')
pdf.set_auto_page_break(auto=False, margin=0)

df = pd.read_csv('topics.csv')

for index, row in df.iterrows():
    pdf.add_page()

    # add header
    pdf.set_font(family='Times', style='B', size=22)
    pdf.set_text_color(100, 100, 100)

    pdf.cell(w=0, h=12, txt=f'{row["Topic"]}', align='L', ln=1)
    pdf.line(10, 21, 200, 21)

    # add lines
    for x in range(21, 291, 10):
        pdf.line(10, x, 200, x)

    # add footer
    pdf.ln(260)
    pdf.set_font(family='Times', style='I', size=12)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=f'{row["Topic"]}', align='R')

    # add empty pages
    for _ in range(row['Pages']-1): 
        pdf.add_page()

        # add lines
        for x in range(10, 285, 10):
            pdf.line(10, x, 200, x)

        # add footer
        pdf.ln(272)
        pdf.set_font(family='Times', style='I', size=12)
        pdf.set_text_color(100, 100, 100)
        pdf.cell(w=0, h=12, txt=f'{row["Topic"]}', align='R')

pdf.output('output.pdf')