from fastapi import APIRouter, Body, Query
from schemas.hotels import Hotel, HotelPATCH
 
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
def create_hotel(hotel_data: Hotel = Body(openapi_examples={
    "1":{
            'summary': 'Россия - Москва - Отель:Grand', 
            'value': {
                'contry': 'Россия',
                'city': 'Москва',
                'name':'Grand'
            }
        },
    "2":{
            'summary': 'ОАЭ - Дубай - Отель:Laky', 
            'value': {
                'contry': 'ОАЭ',
                'city': 'Дубай',
                'name':'Laky'
            }
        },
    })):
    global hotels
    hotels.append({
        "id": hotels[-1]["id"] + 1,
        "contry": hotel_data.contry,
        "city": hotel_data.city,
        "name": hotel_data.name,
    })
    return {"status": "OK"}

@router.put("/{hotel_id}")
def put_hotel(hotel_id: int, hotel_data: Hotel):
    global hotels
    
    for hotel in hotels:
        if hotel_id and hotel_data.contry and hotel_data.city and hotel_data.name and hotel['id'] == hotel_id:
            hotel['name'] = hotel_data.name
            hotel['city'] = hotel_data.city
            hotel['contry'] = hotel_data.contry
            return {"status": "OK"}
        else:
            continue
    return  {"status": "Не OK"}
    
@router.patch("/{hotel_id}")
def patch_hotel(
        hotel_id: int, 
        hotel_data:HotelPATCH
    ):
    global hotels
    for hotel in hotels:
        if hotel['id'] == hotel_id:
            hotel['name'] = hotel_data.name
            hotel['city'] = hotel_data.city
            hotel['contry'] = hotel_data.contry
            return {"status": "OK"}
        else:
            continue
    return  {"status": "Не OK"}
 

@router.delete("/{hotel_id}")
def delete_hotel(hotel_id: int):
    global hotels
    hotels = [hotel for hotel in hotels if hotel["id"] != hotel_id]
    return {"status": "OK"}
