# -*- coding: utf-8 -*-
{
    'name': "EventosSolidaridad",

    'summary': """
        Módulo para gestionar eventos solidarios, incluyendo participantes, tareas y encuestas.
        """,

    'description': """
        Este módulo ayuda a organizar y gestionar eventos solidarios.
        Las características incluyen la gestión de detalles del evento, participantes, tareas relacionadas y encuestas de satisfacción.
    """,

    'author': "Esperanza Solidaria",
    'website': "http://www.esperanzasolidaria.com",

    # Categorías pueden usarse para filtrar módulos en la lista de módulos
    # Ver https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # para la lista completa
    'category': 'Uncategorized',
    'version': '0.1',

    # cualquier módulo necesario para que este funcione correctamente
    'depends': ['base', 'project'],

    # siempre cargado
    'data': [
        'views/views.xml',
    ],
    # solo cargado en modo de demostración
    'demo': [
        'demo/demo.xml',
    ],
}
