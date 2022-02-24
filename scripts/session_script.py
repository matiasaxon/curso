from xmlrpc import client

url = 'https://matiasaxon-curso-desarrollo-1-4293416.dev.odoo.com'
db = 'matiasaxon-curso-desarrollo-1-4293416'
username = 'admin'
password = 'admin'

#Estos son los datos que se pueden consultar sin necesidad de usuario y contraseña
common = client.ServerProxy("{}/xmlrpc/2/common".format(url))
print(common.version())

#Authenticamos una connección con el servidor mediante usuario y contraseña, nos imprime el UID (usuario id)
uid = common.authenticate(db, username, password, {})
print(uid)

#Comprobamos si tenemos accesos de escritura con este usuario
models = client.ServerProxy("{}/xmlrpc/2/object".format(url))

model_access = models.execute_kw(db, uid, password,
                                'academy.session', 'check_access_rights',
                                ['write'], {'raise_exception' : False})

print(model_access)


#A continuación buscaremos todos los cursos que están en nivel intermedio y principiante
courses = models.execute_kw(db, uid, password,
                             'academy.curso', 'search_read',
                             [[['level', 'in', ['intermediate', 'beginner']]]])

print(courses)

#Obtenedremos el id del curso que necesitamos modificar

course = models.execute_kw(db, uid, password,
                           'academy.curso', 'search',
                           [[['name', '=', 'Accounting 200']]])

print(course)



#obtendremos los campos del modelo academy.session, filtrando los que son obligatorios 
session_fields = models.execute_kw(db, uid, password,
                                   'academy.session', 'fields_get',
                                   [], {'attributes': ['string', 'type', 'required']})

print(session_fields)

#Ahora  tenemos toda la información para crear una sessión
new_session = models.execute(db, uid, password, 
                            'academy.session', 'create',
                            [
                                {
                                    'course_id': course[0],
#                                    'state': 'open',
                                    'duration': 5,
                                }
                                    
                            ]
                            )
print(new_session)
