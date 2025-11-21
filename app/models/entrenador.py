from app.database import db

class Entidad(db.Model):
    __tablename__ = "entrenador"
     id = Column(Integer, primary_key=True)