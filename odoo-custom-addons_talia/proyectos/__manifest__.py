{
    'name': "Proyectos",
    'version': '1.0',
    'depends': ['base'],
    'author': "Tu Nombre",
    'category': 'Tools',
    'summary': 'Gestión de proyectos para la ONG',
    'description': """
    Módulo para gestionar proyectos y tareas en una ONG.
    """,
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
    ],
    'installable': True,
    'application': True,
}
