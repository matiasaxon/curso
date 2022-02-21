#-*- coding: utf-8 -*-
from odoo import http

class Academy(http.Controller):
    @http.route('/academy/', auth='public', website=True)
    def index(self, **kw):
        return "Hello, world"
    
    @http.route('/academy/cursos', auth='public', website=True)
    def cursos(self, **kw):
        cursos = http.request.env['academy.curso'].search([])
        return http.request.render('odoo_academy.curso_website',{
            'cursos': cursos,
        })
    
    @http.route('/academy/<model("academy.session"):session>/', auth='public', website=True)
    def session(self, session):
        return http.request.render('odoo_academy.session_website', {
            'session': session,
        })