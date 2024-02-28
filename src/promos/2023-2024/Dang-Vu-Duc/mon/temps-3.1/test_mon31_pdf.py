import PyPDF2

pdfFile = open('PDF test 2.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFile)
print(pdfReader.numPages)

page = pdfReader.getPage(0)
print(page.extractText())

pdfFile.close()

class PDF_Tools():
    def combine_pdf(self, list_pdf: list, name_merged_file: str):
        pdf_writer = PyPDF2.PdfFileWriter()
        list_pdf_objects = []
        for pdf_name in list_pdf:
            pdf_file = open(pdf_name, 'rb')
            list_pdf_objects.append(PyPDF2.PdfFileReader(pdf_file))
        for pdf_object in list_pdf_objects:
            for page_num in range(pdf_object.numPages):
                page_object = pdf_object.getPage(page_num)
                pdf_writer.addPage(page_object)
        new_pdf = open(name_merged_file, 'wb')
        pdf_writer.write(new_pdf)
        new_pdf.close()
    
    def rotate_pages(self, pdf_name: str, list_num_pages: list, rotation: int, name_new_file: str):
        pdf_file = open(pdf_name, 'rb')
        pdf_reader = PyPDF2.PdfFileReader(pdf_file)
        pdf_writer = PyPDF2.PdfFileWriter()
        for num_page in range(pdf_reader.numPages):
            page_object = pdf_reader.getPage(num_page)
            if num_page in list_num_pages:
                page_object.rotateClockwise(rotation)
            pdf_writer.addPage(page_object)
        new_pdf = open(name_new_file, 'wb')
        pdf_writer.write(new_pdf)
        new_pdf.close()
    
    def overlay_pages(self, pdf_name: str, pdf_name_overlay: str, list_num_pages: list, name_new_file: str):
        pdf_file = open(pdf_name, 'rb')
        pdf_reader = PyPDF2.PdfFileReader(pdf_file)
        pdf_writer = PyPDF2.PdfFileWriter()
        for num_page in range(pdf_reader.numPages):
            if num_page not in list_num_pages:
                page_object = pdf_reader.getPage(num_page)
                pdf_writer.addPage(page_object)
            else:
                pdf_file_overlay = open(pdf_name_overlay, 'rb')
                pdf_reader_overlay = PyPDF2.PdfFileReader(pdf_file_overlay)
                page_overlay = pdf_reader_overlay.getPage(0)
                page_object = pdf_reader.getPage(num_page)
                page_overlay.mergePage(page_object)
                pdf_writer.addPage(page_overlay)
        new_pdf = open(name_new_file, 'wb')
        pdf_writer.write(new_pdf)
        new_pdf.close()

    def encrypt(self, pdf_name: str, password: str, name_encrypted_file):
        pdf_file = open(pdf_name, 'rb')
        pdf_reader = PyPDF2.PdfFileReader(pdf_file)
        pdf_writer = PyPDF2.PdfFileWriter()
        for page_num in range(pdf_reader.numPages):
            page_object = pdf_reader.getPage(page_num)
            pdf_writer.addPage(page_object)
        pdf_writer.encrypt(password)
        new_pdf = open(name_encrypted_file, 'wb')
        pdf_writer.write(new_pdf)
        new_pdf.close()
    
    def reorder(self, pdf_name: str, list_new_order: list, name_reordered_file: str):
        pdf_file = open(pdf_name, 'rb')
        pdf_reader = PyPDF2.PdfFileReader(pdf_file)
        pdf_writer = PyPDF2.PdfFileWriter()
        for num_page in list_new_order:
            page_object = pdf_reader.getPage(num_page)
            pdf_writer.addPage(page_object)
        new_pdf = open(name_reordered_file, 'wb')
        pdf_writer.write(new_pdf)
        new_pdf.close()