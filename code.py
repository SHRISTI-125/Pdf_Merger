import PyPDF2

pdf=['Supervised_Learning.pdf','Unsupervised Learning.pdf']
combo = PyPDF2.PdfFileMerger()

for i in pdf:
    combo.append(i)
combo.write("2Concepts.pdf")
combo.close()
