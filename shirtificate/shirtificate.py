from fpdf import FPDF


pdf = FPDF()
pdf.add_page()
pdf.set_font("helvetica", style="B", size=32)
pdf.cell(w=0, text="CS50 Shirtificate", align="c")
pdf.ln(40)
pdf.image("shirtificate.png", w = pdf.epw)
pdf.set_y(100)
pdf.set_font_size(24)
pdf.set_text_color(255, 255, 255)
pdf.cell(w = 0, align = 'c', text = input("Name: ").strip() + " took CS50")
pdf.output("shirtificate.pdf")


# i tried to use subclass but the checker didn't exit with 0
# class PDF(FPDF):
#     def header(self):
#         self.set_font("helvetica", style="B", size=32)
#         self.cell(w=0, text="CS50 Shirtificate", align="c")
#         self.ln(40)
#         self.image("shirtificate.png", w = self.epw)

