# inventario_solidaridad/__manifest__.py
{
    'name': "Gestión de Inventario Esperanza Unida",
    'summary': "Gestiona los productos almacenados de Esperanza Unida.",
    'description': """
        Este módulo permite gestionar los productos almacenados en diversos almacenes de Esperanza Unida,
        clasificados por categorías como ropa, alimentos y albergue.
    """,
    'author': "Esperanza Unida",
    'website': "http://www.esperanzaunida.org",
    'category': 'Inventory',
    'version': '0.1',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
