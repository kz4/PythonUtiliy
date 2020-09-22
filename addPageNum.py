import PyPDF2
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
  
def add_page_number(page_number, pageObj): 
    packet = io.BytesIO()
    # create a new PDF with Reportlab
    can = canvas.Canvas(packet, pagesize=letter)
    can.drawString(300, 10, "-- " + page_number + " --")
    can.save()

    # move to the beginning of the StringIO buffer
    packet.seek(0)
    new_pdf = PyPDF2.PdfFileReader(packet)

    pageObj.mergePage(new_pdf.getPage(0))
      
    return pageObj 
  
def main(): 
    origFileName = 'yourFileName.pdf'      
    newFileName = 'page_number.pdf'
      
    # creating pdf File object of original pdf 
    pdfFileObj = open(origFileName, 'rb') 

    pdfFileWithPageNumObj = open(newFileName, 'wb') 
      
    # creating a pdf Reader object 
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 
  
    # creating a pdf writer object for new pdf 
    pdfWriter = PyPDF2.PdfFileWriter() 
      
    with pdfFileWithPageNumObj as output_file:
        # adding page number to each page
        for page in range(pdfReader.numPages): 
            wmpageObj = add_page_number(str(page + 1), pdfReader.getPage(page))           
            pdfWriter.addPage(wmpageObj) 
            pdfWriter.write(pdfFileWithPageNumObj)
  
    # newFile = open(newFileName, 'wb')       
    # pdfWriter.write(pdfFileWithPageNumObj) 
  
    pdfFileObj.close() 
    pdfFileWithPageNumObj.close() 
  
if __name__ == "__main__": 
    main() 
