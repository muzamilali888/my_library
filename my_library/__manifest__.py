{
    'name': "My library",
    'summary': "Manage books easily",
    'description': """ 
Manage Library 
============== 
Description related to library. 
""",
    'author': "muzammil ali",
    'website': "http://www.example.com",
    'category': 'Uncategorized',
    'version': '13.0.1',
    'depends': ['base'],
    'data': ['views/library_book.xml',
             'views/library_book_categ.xml',
             'views/res_partner.xml',
             'views/library_member.xml',
             'security/groups.xml',
             'security/ir.model.access.csv'
             ],
    'demo': ['demo.xml'],
}
