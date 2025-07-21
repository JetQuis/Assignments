# Recipes controller

from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response
from ..models import models, schemas

def create(db: Session, recipe: schemas.RecipeCreate):
    db_recipe = models.Recipe(
        name=recipe.name,
        size=recipe.size,
        cost=recipe.cost
    )
    db.add(db_recipe)
    db.commit()
    db.refresh(db_recipe)
    return db_recipe