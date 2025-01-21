from fastapi import APIRouter, Body, Query

router = APIRouter(prefix="/hotels", tags=["Отели"])

hotels = [
    {"id": 1, "contry": 'Россия',"city": 'Москва', "name":'Grand'},
    {"id": 2, "contry": 'ОАЭ',"city": 'Дубай', "name":'Laky'},
    {"id": 3, "contry": 'США',"city": 'Бостон', "name":'Number 1'},
    
]

@router.get("")
def get_hotels(
    id: int| None = Query(None,description="Айдишник"),
    name: str | None = Query(None,description="Название отеля"),
):
    hotels_ =[]
    for hotel in hotels:
        if id and hotel['id'] != id:
            continue
        if name and hotel['name'] != name:
            continue
        hotels_.append(hotel)
        
    return hotels_

@router.post("")
def create_hotel(
        contry: str = Body(embed=True),
        name: str = Body(embed=True),
        city: str = Body(embed=True)
):
    global hotels
    hotels.append({
        "id": hotels[-1]["id"] + 1,
        "contry": contry,
        "city": city,
        "name": name,
    })
    return {"status": "OK"}

@router.put("/{hotel_id}")
def put_hotel(
        hotel_id: int, 
        name:str = Body(description="Название отеля"),
        city:str = Body(description="Город"),
        contry: str = Body(description="Название страны")
    ):
    global hotels
    
    for hotel in hotels:
        if hotel_id and contry and city and name and hotel['id'] == hotel_id:
            hotel['name'] = name
            hotel['city'] = city
            hotel['contry'] = contry
            return {"status": "OK"}
        else:
            continue
    return  {"status": "Не OK"}
    
@router.patch("/{hotel_id}")
def patch_hotel(
        hotel_id: int, 
        name:str | None = Body(None,description="Название отеля"),
        city:str | None  = Body(None,description="Город"),
        contry: str | None = Body(None,description="Название страны"),
    ):
    global hotels
    for hotel in hotels:
        if hotel['id'] == hotel_id:
            hotel['name'] = name
            hotel['city'] = city
            hotel['contry'] = contry
            return {"status": "OK"}
        else:
            continue
    return  {"status": "Не OK"}
 

@router.delete("/{hotel_id}")
def delete_hotel(hotel_id: int):
    global hotels
    hotels = [hotel for hotel in hotels if hotel["id"] != hotel_id]
    return {"status": "OK"}
