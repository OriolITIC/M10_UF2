{
    'name': "Inventario Solidaridad",
    'summary': "Gestión de inventarios para la ONG Esperanza Unida",
    'description': """
        Este módulo permite a la ONG Esperanza Unida gestionar sus productos almacenados según la categoría correspondiente.
    """,
    'author': "Esperanza Unida",
    'website': "http://www.esperanzaunida.org",
    'category': 'Inventory',
    'version': '1.0',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'data/data.xml',
    ],
    'installable': True,
    'application': True,
}
