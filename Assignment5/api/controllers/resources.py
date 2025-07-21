# Resources controller

from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response
from ..models import models, schemas

def create(db: Session, resource: schemas.ResourceCreate):
    db_resource = models.Resource(
        name=resource.name,
        quantity=resource.quantity
    )
    db.add(db_resource)
    db.commit()
    db.refresh(db_resource)
    return db_resource

