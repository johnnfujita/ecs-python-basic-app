from fastapi import APIRouter, HTTPException, Depends, status, Response
from .. import schemas, database, models, oauth2
from typing import List
from sqlalchemy.orm import Session


router = APIRouter(
    prefix="/items",
    tags=["Items"],
    
)

@router.post("/", status_code=status.HTTP_201_CREATED)
# YOU CAN DEFINE WHAT ATTRIBUTES WILL BE RETURNED IN THE RESPONSE when you define response_model and choose a pydantic schema
def create_post(item: schemas.ShowItem, db: Session = Depends(database.get_db)):
    
    new_item = models.Item(title=item.title, description=item.description,user_id=1)
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return new_item

@router.delete("/{id}", status_code=200 )
def destroy(id, db: Session = Depends(database.get_db)):
    queried_item = db.query(models.Item).filter(models.Item.id == id)
    if not queried_item.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"item {id} not found")
    queried_item.delete(synchronize_session=False)
    db.commit()
    return {"item": id, "status": "deleted"}


@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED)
def update_item(id, item: schemas.Item, db: Session = Depends(database.get_db)):
    queried_item = db.query(models.Item).filter(models.Item.id == id)
    if not queried_item.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"item {id} not found")
    queried_item.update(item)
    db.commit()
    return {"Status": "Update Successfull"}


@router.get("/", response_model=List[schemas.Item])
def all_item(db: Session = Depends(database.get_db), current_user: schemas._UserShow = Depends(oauth2.get_current_user)):
    items = db.query(models.Item).all()
    return items

@router.get("/{id}", status_code=200,  response_model=schemas.Item)
def get_item(id, response: Response, db: Session = Depends(database.get_db)):
    item = db.query(models.Item).filter(models.Item.id == id).first()
    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"item with the id {id} not found")
        #response.status_code = status.HTTP_404_NOT_FOUND
        #return {"detail": f"Item {id} is not available"}
    return item