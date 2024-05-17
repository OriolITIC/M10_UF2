# -*- coding: utf-8 -*-
{
    'name': "SeguimientoImpactoSocial",

    'summary': """
        Módulo para gestionar y seguir el impacto social de los proyectos y actividades de una ONG.
    """,

    'description': """
        Este módulo permite a las ONGs gestionar y realizar un seguimiento detallado del impacto social de sus proyectos y actividades. Incluye la gestión de indicadores, resultados y beneficiarios asociados a cada impacto social.
    """,

    'author': "Esperanza Solidaria",
    'website': "http://www.esperanzasolidaria.com",

    'category': 'Impacto Social',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'project'],

    # always loaded
    'data': [
        #'security/ir.model.access.csv',
        'views/views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
