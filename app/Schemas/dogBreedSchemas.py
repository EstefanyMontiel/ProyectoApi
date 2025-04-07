
from typing import Optional
from pydantic import BaseModel

class DogBreed(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    size: Optional[str] = None
    energy_level: Optional[str] = None

class CreateDogBreed(BaseModel):  # Ahora también incluye ID manual
    id: int
    name: str
    description: Optional[str] = None
    size: Optional[str] = None
    energy_level: Optional[str] = None
   
class UpdateDogBreed(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    size: Optional[str] = None
    energy_level: Optional[str] = None
   