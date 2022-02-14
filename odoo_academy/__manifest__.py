#-*- coding: utf-8 -*-

{
    'name': 'Odoo Academy',
    
    'Summary': """Academy app to manage Training""",
    
    'description': """
        Academy Module to manege Training:
        - Courses
        -Sessions
        - Attendees
        """,
    
    'author': 'Odoo',
    
    'license': 'LGPL-3',
    
    'website': 'wwww.axonsoftware.cl',
    
    'category': 'Training',
    
    'version': "0.1",
    
    'depends': ['base'],
    
    'data': [
        'security/academy_security.xml',
        'security/ir.model.access.csv',
        'views/academy_menuitems.xml',
        'views/course_views.xml',
        'views/session_views.xml',
        
    ],
    
    'demo': [
        'demo/academy_demo.xml',
    ],
}