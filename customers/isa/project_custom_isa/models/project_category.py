# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2011-2013 ISA s.r.l. (<http://www.isa.it>).
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

from openerp import fields, models, api


class project_category(models.Model):

    _inherit = 'project.category'
    _rec_name = 'code'
    _order = 'name'

    code = fields.Char(string='Code', size=2, select=True)
    category_team_ids = fields.One2many('project.category.team',
                                        'project_category_id',
                                        string='Category Team Members')

    @api.multi
    @api.depends('name', 'code')
    def name_get(self):
        res = []
        for record in self:
            name = record.name or ''
            code = record.code or '#'
            item_desc = code + ' - ' + name
            res.append((record.id, item_desc))
        return res

    @api.model
    def name_search(self, name, args=None, operator='ilike', limit=100):
        args = args or []

        recs = self.search(['|',
                           ('code', operator, name),
                           ('name', operator, name)] + args,
                           limit=limit)

        return recs.name_get()
