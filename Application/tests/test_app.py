# from flask import url_for
# from Application import tests
# from flask_testing import TestCase
# from app import app, db, Register

# class TestBase(TestCase):
#     def create_app(self):
#         app.config.update(SQLALCHEMY_DATABASE_URI='mysql+pymysql://squid@flaskdb:flaskappoctopus123!@flaskdb.mysql.database.azure.com:3306/appdb', 
#         SECRET_KEY='saidwqneoqneoiq', DEBUG=True, WTF_CSRF_ENABLED=False)
#         return app

#     def setup(self):
#         db.create_all()
#         testservice = Services(servicename='CyberGhost', company='Cyber Company', isCompromised=True)
#         db.session.add(testservice)
#         db.session.commit()
    
#     def bringdown(self):
#         db.session.remove()
#         db.drop_all()

# class TestRead(TestBase):
#     def testhomeget(self):
#         response = self.client.get(url_for('read'))
#         self.assertEqual(response.status_code, 200)
#         self.assertIn('1 CyberGhost Cyber Company 1', response.data)

# class TestView(TestBase):
#     def testhomeget(self):
#         response = self.client.get(url_for('read'))
#         self.assertEqual(response.status_code, 200)
#         self.assertIn(index.html, response.data)