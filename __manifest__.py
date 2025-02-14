{
  'name':'Custom Product module',
  'version':'1.0',
  'author':'Nyein Chan Lay',
  'depends':['base','web'],
  'assets':{
    'web.assets_backend':[
      'custom_product_module/static/src/main.js',
      'custom_product_module/static/src/components/*.js',
      'custom_product_module/static/src/templates/*.xml',
    ]
  },
  'data':[
    'security/ir.model.access.csv',
    'views/custom_product_views.xml',
  ],
  'installable':True,
  'application':True
}