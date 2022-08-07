{
    'name': "Hospital",

    'summary': """Hospital""",

    'author': "Andrii Zemlianyi",
    # 'website': "https://odoo.school",

    'category': 'Human Resources',
    'version': '15.0.1.0.5',

    'depends': ['base'],

    'data': [
        'security/ir.model.access.csv',
        'views/hr_hospital_menus.xml',
        'views/contact_person_views.xml',
        'views/disease_type_views.xml',
        'views/patient_test_views.xml',
        'views/personal_doctor_history_views.xml',
        'views/test_type_views.xml',
        'views/diagnosis_views.xml',
        'views/disease_views.xml',
        'views/hr_hospital_menus.xml',
        'views/sample_type_views.xml',
        'views/visit_views.xml',
        'report/doctor_report.xml',
        'report/doctor_templates.xml',
        'views/doctor_views.xml',
        'views/patient_views.xml',
        'data/hr_hospital_data.xml',
        'wizard/set_personal_doctor_view.xml'
    ],

    # 'demo': [
    #     'demo/hr_hospital_demo.xml',
    # ],

    'license': 'LGPL-3',
    'installable': True,
    'auto_install': False,
}
