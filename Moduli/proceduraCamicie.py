#import PyPDF2
#pdf_file = open('C:\\Users\\orlan\\Documents\\Coding\\Python\\Sapienza\\Pergamene\\masters\\camiciaMaster.pdf')
#read_pdf = PyPDF2.PdfReader(pdf_file)

#Reading PDF Files
from pdfrw import PdfReader

def get_pdf_info(path):
    pdf = PdfReader(path)
    #print(pdf.keys())
    print(pdf.info)
    #print(pdf.root.keys())
    print('pdf has {} pages'.format(len(pdf.pages)))
#if __name__ == '__main__':
get_pdf_info('C:\\Users\\orlan\\Documents\\Coding\\Python\\Sapienza\\Pergamene\\masters\\camiciaMaster.pdf')