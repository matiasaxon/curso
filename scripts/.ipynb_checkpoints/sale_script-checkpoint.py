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
                                'sale.order', 'check_access_rights',
                                ['write'], {'raise_exception' : False})

print(model_access)


#obtenemos todas las órdenes que  estsán en estado borrador

draft_quotes = models.execute_kw(db, uid, password,
                                 'sale.order', 'search',
                                 [[['state', '=', 'draft']]])

print(draft_quotes)

#una vez obtenidas las ordenes en estado borrador, vamos a llamar a action_confirm, para que las confirme y les cambie el estado

if_confirmed = models.execute_kw(db, uid, password, 
                                 'sale.order', 'action_confirm',
                                 [draft_quotes])

print(if_confirmed)

