from sqlalchemy import Column, Integer, String
from app.Database.DB import Base  # Asegúrate de que Base esté correctamente importado

class DogBreed(Base):
    __tablename__ = "dog_breeds"

    id = Column(Integer, primary_key=True, index=True)           # ID único de la raza
    name = Column(String(50), nullable=False)                    # Nombre de la raza
    description = Column(String(255), nullable=True)             # Descripción general
    size = Column(String(30), nullable=True)                     # Tamaño: pequeño, mediano, grande
    energy_level = Column(String(30), nullable=True)             # Nivel de energía: bajo, medio, alto


