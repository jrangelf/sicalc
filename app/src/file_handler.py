def handle_uploaded_file(f):
	print("#=======handle_upload_file===========")
	print("#-----f-----------")
	print(f)
	diretorio = '/Users/rangel/Desktop/'
	nome = 'teste_de_upload'
	extensao = '.txt'
	arquivo = diretorio+nome+extensao

	for pedaco in f.chunks():
		print("pedaco: ", pedaco)
		



	with open(arquivo, 'wb+') as destination:
		for chunk in f.chunks():
			print("#----chunk-------------")
			print(chunk)
			destination.write(chunk)