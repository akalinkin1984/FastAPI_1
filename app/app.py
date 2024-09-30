import crud
import fastapi
from sqlalchemy.future import select

import models
import schema
from constants import STATUS_SUCCESS_RESPONSE
from dependencies import SessionDependency
from lifespan import lifespan

app = fastapi.FastAPI(
    title="Advertisement service",
    version="0.0.1",
    description="...",
    lifespan=lifespan
)


@app.get("/advertisement/{adv_id}", response_model=schema.GetAdvResponse)
async def get_adv(adv_id: int, session: SessionDependency):
    adv = await crud.get_item(session, models.Advertisement, adv_id)
    return adv.dict


@app.post("/advertisement", response_model=schema.CreateAdvResponse)
async def create_adv(adv_json: schema.CreateAdvRequest, session: SessionDependency):
    adv = models.Advertisement(**adv_json.dict())
    adv = await crud.add_item(session, adv)
    return adv.id_dict


@app.patch("/advertisement/{adv_id}", response_model=schema.UpdateAdvResponse)
async def update_adv(adv_id: int, adv_json: schema.UpdateAdvRequest, session: SessionDependency):
    adv = await crud.get_item(session, models.Advertisement, adv_id)
    adv_patch = adv_json.dict(exclude_unset=True)

    for field, value in adv_patch.items():
        setattr(adv, field, value)
    await crud.add_item(session, adv)
    return adv.id_dict


@app.delete("/advertisement/{adv_id}", response_model=schema.DeleteAdvResponse)
async def delete_adv(adv_id: int, session: SessionDependency):
    await crud.delete_item(session, models.Advertisement, adv_id)
    return STATUS_SUCCESS_RESPONSE


@app.get("/advertisement", response_model=schema.SearchAdvResponse)
async def search_adv(qs_params: str, session: SessionDependency):
    query = (select(models.Advertisement).
             filter(models.Advertisement.title.contains(qs_params) |
                    models.Advertisement.description.contains(qs_params)))
    data = await session.execute(query)
    res = data.scalars().all()

    return {'result': res}
