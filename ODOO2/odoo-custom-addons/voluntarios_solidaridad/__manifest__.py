{
    'name': "Gestión de Voluntarios Esperanza Solidaria",
    'summary': """
        Gestiona los voluntarios y sus actividades en Esperanza Solidaria.""",
    'description': """
        Este módulo permite a una Esperanza Solidaria a sus voluntarios, incluyendo el registro de voluntarios,
        asignación de tareas, seguimiento de horas de servicio, y más.
    """,
    'author': "Esperanza Solidaria",
    'website': "http://www.esperanzasolidaria.com",
    'category': 'Nonprofit',
    'version': '0.1',
    'depends': ['base'],
    'data': [
        'views/activity_views.xml',
        'views/department_views.xml',
        'views/estadistica_views.xml',
        'views/volunteer_views.xml',
        'views/menu_views.xml'     
    ],
    'demo': [
        'demo/demo.xml',
    ],
}
