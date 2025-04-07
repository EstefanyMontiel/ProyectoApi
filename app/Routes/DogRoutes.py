from fastapi import APIRouter, HTTPException, Query, Depends
from typing import List
from sqlalchemy.orm import Session as Database
from sqlalchemy.exc import SQLAlchemyError

from app.Schemas.dogBreedSchemas import DogBreed, CreateDogBreed, UpdateDogBreed # type: ignore
from app.Database.DB import get_db
from app.Models.dogBreedEntity import DogBreed as DogBreedModel

router = APIRouter(
    prefix="/DogBreeds",
    tags=["DogBreeds"]
)

# GET por ID
@router.get("/{id}", response_model=DogBreed)
def get_dog_breed_by_id(id: int, db: Database = Depends(get_db)) -> DogBreed:
    try:
        dog_breed = db.query(DogBreedModel).filter(DogBreedModel.id == id).first()
        if not dog_breed:
            raise HTTPException(status_code=404, detail="Dog breed not found")
        return dog_breed
    except HTTPException as e:
        raise e
    except Exception as e:
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=f"Internal server error: {e}")

# GET con filtro opcional y paginación
@router.get("/", response_model=List[DogBreed])
def get_dog_breeds(
    name: str = Query(None),
    page: int = Query(1, ge=1),
    size: int = Query(10, ge=1),
    db: Database = Depends(get_db)
) -> List[DogBreed]:
    try:
        query = db.query(DogBreedModel)
        if name:
            query = query.filter(DogBreedModel.name.ilike(f"%{name}%"))
        results = query.offset((page - 1) * size).limit(size).all()
        return results
    except HTTPException as e:
        raise e
    except Exception as e:
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=f"Internal server error: {e}")


# POST
@router.post("/", response_model=DogBreed, status_code=201)
def create_dog_breed(dog_breed: CreateDogBreed, db: Database = Depends(get_db)) -> DogBreed:
    try:
        existing = db.query(DogBreedModel).filter(DogBreedModel.id == dog_breed.id).first()
        if existing:
            raise HTTPException(status_code=400, detail="Dog with this ID already exists")

        new_dog_breed = DogBreedModel(
            id=dog_breed.id,
            name=dog_breed.name,
            description=dog_breed.description,
            size=dog_breed.size,
            energy_level=dog_breed.energy_level
        )
        db.add(new_dog_breed)
        db.commit()
        db.refresh(new_dog_breed)
        return new_dog_breed
    except HTTPException as e:
        raise e
    except SQLAlchemyError:
        db.rollback()
        raise HTTPException(status_code=500, detail="Database error")
    except Exception as e:
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=f"Internal server error: {e}")

# PUT
@router.put("/{id}", response_model=DogBreed)
def update_dog_breed(id: int, dog_breed: UpdateDogBreed, db: Database = Depends(get_db)) -> DogBreed:
    try:
        db_dog_breed = db.query(DogBreedModel).filter(DogBreedModel.id == id).first()
        if not db_dog_breed:
            raise HTTPException(status_code=404, detail="Dog breed not found")

        for key, value in dog_breed.model_dump(exclude_unset=True).items():
            setattr(db_dog_breed, key, value)

        db.commit()
        db.refresh(db_dog_breed)
        return db_dog_breed
    except HTTPException as e:
        raise e
    except SQLAlchemyError:
        db.rollback()
        raise HTTPException(status_code=500, detail="Database error")
    except Exception as e:
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=f"Internal server error: {e}")

# DELETE
@router.delete("/{id}")
def delete_dog_breed(id: int, db: Database = Depends(get_db)):
    try:
        dog_breed = db.query(DogBreedModel).filter(DogBreedModel.id == id).first()
        if not dog_breed:
            raise HTTPException(status_code=404, detail="Dog breed not found")

        db.delete(dog_breed)
        db.commit()
        return {"message": "Dog breed deleted"}
    except HTTPException as e:
        raise e
    except SQLAlchemyError:
        db.rollback()
        raise HTTPException(status_code=500, detail="Database error")
    except Exception as e:
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=f"Internal server error: {e}")