
from fastapi import FastAPI
# from .item.database import engine
# from .item import models


# from  .item.routers import authentication, item, user

app = FastAPI()

@app.get("/")
def home():
    return {"home": "hello"}
# models.Base.metadata.create_all(engine)

# app.include_router(item.router)
# app.include_router(user.router)
# app.include_router(authentication.router)

# the session was actually created in the database.py file by the sessionmaker
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()



# @app.post("/item", status_code=status.HTTP_201_CREATED, tags=["items"])
# # YOU CAN DEFINE WHAT ATTRIBUTES WILL BE RETURNED IN THE RESPONSE when you define response_model and choose a pydantic schema
# def create_post(item: schemas.ShowItem, db: Session = Depends(get_db)):
    
#     new_item = models.Item(title=item.title, description=item.description,user_id=1)
#     db.add(new_item)
#     db.commit()
#     db.refresh(new_item)
#     return new_item

# @app.delete("/item/{id}", status_code=200, tags=["items"])
# def destroy(id, db: Session = Depends(get_db)):
#     queried_item = db.query(models.Item).filter(models.Item.id == id)
#     if not queried_item.first():
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"item {id} not found")
#     queried_item.delete(synchronize_session=False)
#     db.commit()
#     return {"item": id, "status": "deleted"}


# @app.put("/item/{id}", status_code=status.HTTP_202_ACCEPTED, tags=["items"])
# def update_item(id, item: schemas.Item, db: Session = Depends(get_db)):
#     queried_item = db.query(models.Item).filter(models.Item.id == id)
#     if not queried_item.first():
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"item {id} not found")
#     queried_item.update(item)
#     db.commit()
#     return {"Status": "Update Successfull"}


# @app.get("/item", response_model=schemas.Item)
# def all_item(db: Session = Depends(get_db)):
#     items = db.query(models.Item).all()
#     return items

# @app.get("/item/{id}", status_code=200,  response_model=schemas.Item)
# def get_item(id, response: Response, db: Session = Depends(get_db), tags=["items"]):
#     item = db.query(models.Item).filter(models.Item.id == id).first()
#     if not item:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"item with the id {id} not found")
#         #response.status_code = status.HTTP_404_NOT_FOUND
#         #return {"detail": f"Item {id} is not available"}
#     return item


# @app.post("/user", status_code=status.HTTP_201_CREATED,  response_model=schemas._UserShow, tags=["users"])
# def create_user(_user: schemas._User, db: Session = Depends(get_db)):
#     hashed_password = pwd_cxt.hash(_user.password)
#     new_user = models._User(name=_user.name, email=_user.email, password=hashed_password)
#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)
#     return new_user

# @app.get("/user/{id}", status_code=200, response_model=schemas._UserShow, tags=["users"])
# def get_user_by_id(id:int, db: Session =Depends(get_db)):
#     user = db.query(models._User).filter(models._User.id == id).first()
#     if not user:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"user with the id {id} not found")
#     return user


if __name__=="__main__":
    app.run()