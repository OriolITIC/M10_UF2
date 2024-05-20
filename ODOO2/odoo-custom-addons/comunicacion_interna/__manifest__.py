{
    'name': "comunicacion_interna",
    'summary': """
        Gestión de comunicación interna para la organización Esperanza Solidaria.
    """,
    'description': """
        Este módulo permite gestionar la comunicación interna dentro de la organización Esperanza Solidaria. 
        Permite enviar mensajes internos, crear eventos y publicar anuncios para mantener a todos los 
        voluntarios y departamentos informados.
    """,
    'author': "Esperanza Solidaria",
    'website': "http://www.esperanzasolidaria.com",
    'category': 'Recursos Humanos', 
    'version': '0.1',
    'depends': ['base', 'voluntarios_solidaridad'],  
    'data': [
        'views/message_views.xml',
        'views/advertisement_views.xml',
        'views/menu_views.xml'
    ],
    'demo': [
        
    ],
}
