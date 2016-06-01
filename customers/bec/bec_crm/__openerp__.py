# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2013
#    Stefano Siccardi creativiquadrati snc
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'BEC CRM',
    'version': '0.1',
    'category': 'Generic Modules/Others',
    'description': """
Personalizzazioni CRM per BEC
=============================

Il modulo modifica il filtro delle Opportunità (in Vendite)
per rendere più veloce la ricerca.

        """,
    'author': 'ISA S.r.l.',
    'website': 'http://www.isa.it',
    'depends': ['crm', 'base'],
    'data': ['crm_lead_view.xml',
             ],
    'installable': True,
    'active': False,
}