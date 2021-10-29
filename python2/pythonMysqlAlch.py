import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
 

engine = sqlalchemy.create_engine(
    'mysql+mysqlconnector://root@localhost:3306/clase',
    echo=True)
 

Base = declarative_base()
class User(Base):
    __tablename__ = 'usuarios'
 
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    nombre = sqlalchemy.Column(sqlalchemy.String(length=50))
    cc = sqlalchemy.Column(sqlalchemy.String(length=20))
    direccion = sqlalchemy.Column(sqlalchemy.String(length=50))
 
    def __repr__(self):
        return "<User(nombre='{0}', cc='{1}', direccion='{2}')>".format(
                            self.nombre, self.cc, self.direccion)
 
Base.metadata.create_all(engine)
 

Session = sqlalchemy.orm.sessionmaker()
Session.configure(bind=engine)
session = Session()
 

registro = User(nombre='Wilmar Suarez', cc='15373474', direccion='Calle 1 cra 2')
session.add(registro)
session.commit()
 

consulta = session.query(User).filter_by(nombre='Juan Carlos').first()
print('\nRegistro:')
print(consulta)
print('Cedula: {}'.format(consulta.cc))


session.query(User).filter(User.id==6).update({'nombre':'Pepe'},synchronize_session='fetch')
session.commit()
consulta2 = session.query(User).filter_by(id=6).first()

print('\nRegistro 2:')
print(consulta2)