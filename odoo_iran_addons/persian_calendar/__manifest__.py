# -*- coding: utf-8 -*-
# Copyright (C) 2024-Today: Odoo Community Iran
# @author: Odoo Community Iran (https://odoo-community.ir/
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    'name': "Persian Calendar",

    'summary': """
        Persian Calendar""",

    'description': """
       Persian Calendar
    """,

    'author': "https://odoo-community.ir/",
    'website': "https://odoo-community.ir/",
    'category': 'Localization/Iran',
    'version': '1.0.1',
    'depends': ['base', 'web'],
    'assets': {
        'web.assets_backend': [
            'persian_calendar/static/src/js/main.js',
            'persian_calendar/static/src/js/persian-date.js',
            'persian_calendar/static/src/js/farvardin.js',
            'persian_calendar/static/src/js/datetimepicker_service.js',
            'persian_calendar/static/src/js/loader.js',
        ],
        'persian_calendar.calendar_persian':[
            'persian_calendar/static/src/js/format_utils.js',
            'persian_calendar/static/src/js/list.js',
            'persian_calendar/static/src/js/datetime_field.js',
            'persian_calendar/static/src/js/jdatetime.js',
        ]
    }
}