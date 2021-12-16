from app import db, Services, Agencies

# db.create_all()

# dropping tables - 
# SET FOREIGN_KEY_CHECKS=0; DROP TABLE Services; SET FOREIGN_KEY_CHECKS=1;
# SET FOREIGN_KEY_CHECKS=0; DROP TABLE Agencies; SET FOREIGN_KEY_CHECKS=1;


# testservice = Services(servicename='CyberGhost', company='Cyber Company', isCompromised=True)
# db.session.add(testservice)
# db.session.commit()

# testagency = Agencies(agencyname='MI5', service=testservice)
# testagency2 = Agencies(agencyname='GCHQ', service=testservice)
# db.session.add(testagency)
# db.session.add(testagency2)
# db.session.commit()

x = Services.query.get(1)
y = Agencies.query.filter_by(service_id=1).first()
z = Services.query.get(1).id
print(y, type(y))
print(x.servicename, x.company, x.isCompromised, y.agencyname)
print(z)

# testagency=Agencies(agencyname='CIA', service=x)
# db.session.add(testagency)
# db.session.commit()