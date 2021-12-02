# -*- coding: utf-8 -*-
# Part of Thamardaw. See LICENSE file for full copyright and licensing details.

{

    "name": "HIDTCOP",
    "version": "0.1",
    "currency": 'MMK',
    "summary": "HIDTCOP",
    "category": "Industries",
    "description": """
    OKM Iron developed a new Odoo module apps
    This module is used to manage Hospital and Healthcare Management and Clinic Management apps. 
    manage clinic manage Patient hospital in odoo manage Healthcare system ,    
""",

    "depends": ["base"],
    "data": [
    'security/ir.model.access.csv',
    'views/main_menu_file.xml',
    'views/hidtcop_appointment.xml',
    ],
    "author": "HIDTCOP Group",
    "website": "http://www.thamardaw.com",
    "installable": True,
    "application": True,
    "auto_install": False,
    "images": ["static/description/logo.png"],

}


