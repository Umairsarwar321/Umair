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
{
    'name': "Head Project Analysis",
    'summary': """
        This module is give you define head project and task analysis base on head project.""",
    'description': """
        This module is give you define head project and task analysis base on head project.
    """,
    'author': 'Acespritech Solutions Pvt. Ltd.',
    'website': 'http://www.acespritech.com',
    'category': 'Project',
    'version': '14.0.1.0.0',
    'sequence': 1,

    'depends': ['base','project','industry_fsm'],

    'data': [
        'security/ir.model.access.csv',
        'views/head_project.xml',
    ],

    'installable': True,
    'application': True,
    'auto_install': False,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: