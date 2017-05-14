

def addComment(cursor,values):
	query = '''
		insert into comments (surname,name,patronim,email,phone,msg )
		values (?,?,?,?,?)
	'''
	cursor.execute(query,values['surname'],values['name'],values['patronim'],values['email'],values['phone'],values['msg'])
	
def delComment(cursor,id_):
	query = '''
		delete from comments
		where id = ?
	'''
	cursor.execute(query,id_)

def showCountByRegions(region = None):
	query = '''
		select *
		from statByRegions
		where name = ?
	'''
	return cursor.execute(query,region)

def showCountByCities(r_code = None):
	query = '''
		select c.name,count(0)
		from comments comm
			on c.city_code = comm.city
			and c.region_code = ?
		group by c.name
	'''
	return cursor.execute(query,r_code)
