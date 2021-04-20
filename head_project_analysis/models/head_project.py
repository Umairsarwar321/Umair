# -*- coding: utf-8 -*-
#################################################################################
# Author      : Acespritech Solutions Pvt. Ltd. (<www.acespritech.com>)
# Copyright(c): 2012-Present Acespritech Solutions Pvt. Ltd.
# All Rights Reserved.
#
# This program is copyright property of the author mentioned above.
# You can`t redistribute it and/or modify it.
#
#################################################################################
from odoo import fields, models, api
# from odoo.exceptions import ValidationError

class ProjectTask(models.Model):
    _name = "head.project"
    _description = "Program"

    name = fields.Char(string='Head Project')
    # project_ids = fields.One2many('project.project','head_project_id',string="Sub Projects")

class ProjectProject(models.Model):
    _inherit = "project.project"
    _description = "Project Project"

    head_project_id = fields.Many2one("head.project", string='Program')

class ProjectTask(models.Model):
    _inherit = "project.task"
    _description = "Project Task"

    head_project_id = fields.Many2one("head.project", string='Program')

    @api.onchange('project_id')
    def onchange_project_id(self):
        for rec in self:
            return {'domain': {'head_project_id': [('name', '=', rec.project_id.head_project_id.name)]}}

class ReportProjectTask(models.Model):
    _inherit = "report.project.task.user"

    head_project_id = fields.Many2one("head.project", string='Program')

    def _select(self):
        return super(ReportProjectTask, self)._select() + """,
            t.head_project_id as head_project_id
          """

    def _group_by(self):
        return super(ReportProjectTask, self)._group_by() + """,
        t.head_project_id
            """

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: