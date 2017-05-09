

def addComment(cursor,values):
	query = '''
		insert into comments (surname,name,patronim,email,phone,msg )
		values (?,?,?,?,?)
	'''
	cursor.execute(query,*values)
	
def delComment():
	pass

def showCountByRegions():
	pass

def showCountByCities():
	pass

	
