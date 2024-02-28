from test_mon31_pdf import PDF_Tools

test = PDF_Tools()

test.combine_pdf(["PDF test 1.pdf", "PDF test 2.pdf"], "Nouveau PDF.pdf")
test.rotate_pages("PDF test 1.pdf", [0,1,3], 180, "Nouveau PDF2.pdf")
test.overlay_pages("PDF test 2.pdf", "Logo Centrale.pdf", [1, 2, 3, 4, 5], "Nouveau PDF3.pdf")
test.encrypt("PDF test 1.pdf", "motdepasse", "Nouveau PDF4.pdf")
test.reorder("PDF test 1.pdf", [1,0,2,4,3,5], "Nouveau PDF5.pdf")