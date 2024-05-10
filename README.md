# django_ORM
django orm , signal , mapping , manager , tutorials

ROLL BACK TO PREVIOUS MIGRATIONS
    1 - python3 manage.py showmigrations --list
    2 - python3 manage.py migrate 0004_remove_productline_attribute_attributevalue_and_more
    3 - python3 manage.py migrate catalogue zero ==== unapply all migrations before migrating from start , remove migration files