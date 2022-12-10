import webbrowser
from fpdf import FPDF
from glob import glob
from time import sleep
import os

def linkOpen(link):
    webbrowser.open(link)

def createPDF(namePDF, pdf):
    os.chdir("/home/denny/Scaricati")
    imageList = glob("*.png")
    for image in imageList:
        if '(' not in image:
            pdf.add_page()
            pdf.image(image, x=50, y=100, w=70, h=60)
    pdf.output(f"{namePDF}.pdf", "F")

for i in range(1, 925):
    if i > 0:
        print(i)
        linkOpen(f"https://etext-content.gls.pearson-intl.com/eplayer/pdfassets/prod1/145274/31cdabd1-152e-41cc-adbf-c474cce9472b/pages/page0?password=&accessToken=eyJraWQiOiJrMjU0OC4xNjAyOTEzNzczIiwiYWxnIjoiUlM1MTIifQ.eyJzdWIiOiJhNTA5M2VhOGI2NTQ0ZWM4YTkyNDkxOWQ0ZTZmNzFiNCIsIm9jZCI6IjE2NzA2ODEyODkiLCJiaCI6IjExNjE1NTIxMDMiLCJpc3MiOiJJRVMiLCJoY2MiOiJJVCIsInR5cGUiOiJzZSIsImxhbmciOiJpdCIsImV4cCI6MTY3MDY5MjA5MCwiZGV2aWNlaWQiOiJhZjE1ODFmNjVkODJlYWYyZGUwODU5ZDAiLCJpYXQiOjE2NzA2ODEyOTAsImNsaWVudF9pZCI6ImNHbkZFeWlhakdndjJFaGNTaENQQmE3anF3U0ZwU0c1Iiwic2Vzc2lkIjoiMTY1NDczZmItNWMxYi00ODFlLWJhMzUtN2MwNjM3ZDJiZjVmIn0.hqr_JOvCZPiIRizJr9j1S-VLy3yKbbghbAOZciMm6HekF9bAC3dKZV3mzP9HGJoKs4e6KtYsx_n2iSolyjTsBkTfhAhStkMEuW3lraxto79w783u658yREaDi37Og7bVGwD5E7R_kApwupCDduGzr_rnocaaOVBl7wZFYljVbAfmhWlWnU2dLHA2aVma3pa1PnHfskwcZV-yVr7FmQ0e9Yp77EQQRyxy58TDh43EfQn6_MnmXw47vYIHsuJYkkHNFI4hR62xDSAUBVSygj2MUnS2glMfr52xkoEBhqp82jAL_uLxY23qf8ONjNlH_q0nESxezXMQAlsdepafHB_Gyg&formMode=true")
        sleep(1)
       
pdf = FPDF()
createPDF("letteratura ieri oggi e domani 3.1", pdf)
    