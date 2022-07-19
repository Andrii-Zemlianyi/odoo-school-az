{
    'name': "Hospital",

    'summary': """Hospital""",

    'author': "Andrii Zemlianyi",
    # 'website': "http://odoo.school",

    'category': 'Human Resources',
    'version': '15.0.1.0.1w',

    'depends': ['base'],

    'data': [
        'security/ir.model.access.csv',
        'views/hr_hospital_menu.xml',
        'views/diagnosis_views.xml',
        'views/doctor_views.xml',
        'views/patient_views.xml',
        # 'views/patient_card_views.xml',
    ],

    'demo': [
        'demo/hr_hospital_demo.xml',
    ],
    'license': 'LGPL-3',
    'installable': True,
    'auto_install': False,
}
