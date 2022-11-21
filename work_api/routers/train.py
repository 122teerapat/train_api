from fastapi import APIRouter
from pydantic import BaseModel
from typing import Optional

router = APIRouter(
    prefix="/train",
    tags=['Train'],
    responses={ 404 : {'message' : "Not found"}}
)

class station(BaseModel):
    code: str
    stationName: str
    haveConnectSta: bool
    ConnectStaName: Optional[str] = None
    ConnectRoute: Optional[str] = None

class TrainRoute(BaseModel):
    routeName: str
    description: Optional[str] = None
    trainStation: list[station]


TrainRoute_db = {
    1: {
        "Route" : "BTS-SUKUMVIT",
        "Train_Station" : [{"code": "N24","name": "คูคต", "Have_Connect_Station": False},{"code": "N23","name": "สถานีแยกคปอ.2", "Have_Connect_Station": False},
                            {"code": "N22","name": "สถานีพิพิธภัณฑ์กองทัพอากาศ", "Have_Connect_Station": False},
                            {"code": "N21","name": "สถานีโรงพยาบาลภูมิพลอดุลยเดช", "Have_Connect_Station": False},
                            {"code": "N20","name": "สถานีสะพานใหม่", "Have_Connect_Station": False},{"code": "N19","name": "สถานีสายหยุด", "Have_Connect_Station": False},
                            {"code": "N18","name": "สถานีพหลโยธิน 59", "Have_Connect_Station": False},{"code": "N17","name": "สถานีวัดพระศรีมหาธาตุ", "Have_Connect_Station": False},
                            {"code": "N16","name": "สถานีกรมทหารราบที่ 11", "Have_Connect_Station": False},{"code": "N15","name": "สถานีบางบัว", "Have_Connect_Station": False},
                            {"code": "N14","name": "สถานีกรมป่าไม้", "Have_Connect_Station": False},{"code": "N13","name": "สถานีมหาวิทยาลัยเกษตรศาสตร์", "Have_Connect_Station": False},
                            {"code": "N12","name": "สถานีเสนานิคม", "Have_Connect_Station": False},{"code": "N11","name": "สถานีรัชโยธิน", "Have_Connect_Station": False},
                            {"code": "N10","name": "สถานีพหลโยธิน 24", "Have_Connect_Station": False},
                            {"code": "N9","name": "สถานีห้าแยกลาดพร้าว", "Have_Connect_Station": True,"Connect-station":"พหลโยธิน","Connect-Route":"MRT"},
                            {"code": "N8","name": "สถานีหมอชิต", "Have_Connect_Station": True,"Connect-station":"สวนจตุจักร","Connect-Route":"MRT"},
                            {"code": "N7","name": "สถานีสะพานควาย", "Have_Connect_Station": False},{"code": "N5","name": "สถานีอารีย์", "Have_Connect_Station": False},
                            {"code": "N4","name": "สถานีสนามเป้า", "Have_Connect_Station": False},
                            {"code": "N3","name": "สถานีอนุสาวรีย์ชัยสมรภูมิ", "Have_Connect_Station": False},
                            {"code": "N2","name": "สถานีพญาไท", "Have_Connect_Station": True,"Connect-station":"พญาไทย","Connect-Route":"AIRPORT-LINK"},
                            {"code": "N1","name": "สถานีราชเทวี", "Have_Connect_Station": False},
                            {"code": "CEN","name": "สถานีสยาม", "Have_Connect_Station": True,"Connect-station":"สถานีสยาม","Connect-Route":"BTS-SILOM"},
                            {"code": "E1","name": "สถานีชิดลม", "Have_Connect_Station": False},{"code": "E2","name": "สถานีเพลินจิต", "Have_Connect_Station": False},
                            {"code": "E3","name": "สถานีนานา", "Have_Connect_Station": False},
                            {"code": "E4","name": "สถานีอโศก","Have_Connect_Station": True,"Connect-station":"สุขุมวิท","Connect-Route":"MRT"},
                            {"code": "E5","name": "สถานีพร้อมพงษ์", "Have_Connect_Station": False},{"code": "E6","name": "สถานีทองหล่อ", "Have_Connect_Station": False},
                            {"code": "E7","name": "สถานีเอกมัย", "Have_Connect_Station": False},{"code": "E8","name": "สถานีพระโขนง", "Have_Connect_Station": False},
                            {"code": "E9","name": "สถานีอ่อนนุช", "Have_Connect_Station": False},{"code": "E10","name": "สถานีบางจาก", "Have_Connect_Station": False},
                            {"code": "E11","name": "สถานีปุณณวิถี", "Have_Connect_Station": False},
                            {"code": "E12","name": "สถานีอุดมสุข", "Have_Connect_Station": False},{"code": "E13","name": "สถานีบางนา", "Have_Connect_Station": False},
                            {"code": "E14","name": "สถานีแบริ่ง", "Have_Connect_Station": False},
                            {"code": "E15","name": "สถานีสำโรง", "Have_Connect_Station": False},{"code": "E16","name": "สถานีปู่เจ้า", "Have_Connect_Station": False},
                            {"code": "E17","name": "สถานีช้างเอราวัณ", "Have_Connect_Station": False},
                            {"code": "E18","name": "สถานีโรงเรียนนายเรือ", "Have_Connect_Station": False},{"code": "E19","name": "สถานีปากน้ำ", "Have_Connect_Station": False},
                            {"code": "E20","name": "สถานีศรีนครินทร์", "Have_Connect_Station": False},
                            {"code": "E21","name": "สถานีแพรกษา", "Have_Connect_Station": False},{"code": "E22","name": "สถานีสายลวด", "Have_Connect_Station": False},
                            {"code": "E23","name": "สถานีเคหะฯ", "Have_Connect_Station": False},
                         ]
    },

    2:{
        "Route" : "BTS-SILOM",
        "Train_Station" : [{"code": "S12","name": "สถานีบางหว้า","Have_Connect_Station": True,"Connect-station":"บางหว้า","Connect-Route":"MRT"},
                          {"code": "S11","name": "สถานีวุฒากาศ", "Have_Connect_Station": False},{"code": "S10","name": "สถานีตลาดพลู", "Have_Connect_Station": False},
                          {"code": "S9","name": "สถานีโพธิ์นิมิตร", "Have_Connect_Station": False},{"code": "S8","name": "สถานีวงเวียนใหญ่", "Have_Connect_Station": False},
                          {"code": "S7","name": "สถานีกรุงธนบุรี", "Have_Connect_Station": False},
                          {"code": "S6","name": "สถานีสะพานตากสิน", "Have_Connect_Station": False},
                          {"code": "S5","name": "สถานีสุรศักดิ์", "Have_Connect_Station": False},{"code": "S4","name": "สถานีเซนต์หลุยส์", "Have_Connect_Station": False},
                          {"code": "S3","name": "สถานีช่องนนทรี", "Have_Connect_Station": False},
                          {"code": "S2","name": "สถานีศาลาแดง","Have_Connect_Station": True,"Connect-station":"สีลม","Connect-Route":"MRT"},
                          {"code": "S1","name": "สถานีราชดำริ", "Have_Connect_Station": False},
                          {"code": "CEN","name": "สถานีสยาม","Have_Connect_Station": True,"Connect-station":"สถานีสยาม","Connect-Route":"BTS-SUKUMVIT"},
                          {"code": "W1","name": "สถานีสนามกีฬาแห่งชาติ", "Have_Connect_Station": False},
                          ]
    },
    3:{
        "Route" : "AIRPORT-LINK",
        "Train_Station" : [{"code": "A1","name": "สถานีสุวรรณภูมิ", "Have_Connect_Station": False},
                          {"code": "A2","name": "สถานีลาดกระบัง", "Have_Connect_Station": False},
                          {"code": "A3","name": "บ้านทับช้าง", "Have_Connect_Station": False},
                          {"code": "A4","name": "หัวหมาก", "Have_Connect_Station": False},
                          {"code": "A5","name": "รามคำแหง", "Have_Connect_Station": False},
                          {"code": "A6","name": "มักกะสัน","Have_Connect_Station": True,"Connect-station":"เพชรบุรี","Connect-Route":"MRT"},
                          {"code": "A7","name": "ราชปรารถ", "Have_Connect_Station": False},
                          {"code": "A8","name": "พญาไทย","Have_Connect_Station": True,"Connect-station":"สถานีพญาไท","Connect-Route":"BTS-SUKUMVIT"},
                          ]

    },
    4:{
        "Route" : "MRT",
        "Train_Station" : [{"code": "M1","name": "หลักสอง", "Have_Connect_Station": False},{"code": "M2","name": "บางแค", "Have_Connect_Station": False},
                            {"code": "M3","name": "ภาษีเจริญ", "Have_Connect_Station": False},
                          {"code": "M4","name": "เพชรเกษม48", "Have_Connect_Station": False},
                          {"code": "M5","name": "บางหว้า","Have_Connect_Station": True,"Connect-station":"บางหว้า","Connect-Route":"BTS-SILOM"},
                          {"code": "M6","name": "บางไผ่", "Have_Connect_Station": False},{"code": "M7","name": "ท่าพระ", "Have_Connect_Station": False},
                          {"code": "M8","name": "อิสรภาพ", "Have_Connect_Station": False},
                          {"code": "M9","name": "สนามไชย", "Have_Connect_Station": False},
                          {"code": "M10","name": "สามยอด", "Have_Connect_Station": False},{"code": "M11","name": "วัดมังกร", "Have_Connect_Station": False},
                          {"code": "M12","name": "หัวลำโพง", "Have_Connect_Station": False},
                          {"code": "M13","name": "สามย่าน", "Have_Connect_Station": False},
                          {"code": "M14","name": "สีลม","Have_Connect_Station": True,"Connect-station":"สถานีศาลาแดง","Connect-Route":"BTS-SILOM"},
                          {"code": "M15","name": "ลุมพินี", "Have_Connect_Station": False},
                          {"code": "M16","name": "คลองเตย", "Have_Connect_Station": False},{"code": "M17","name": "ศูนย์ฯสิริกิติ์", "Have_Connect_Station": False},
                          {"code": "M18","name": "สุขุมวิท","Have_Connect_Station": True,"Connect-station":"สถานีอโศก","Connect-Route":"MRT"},
                          {"code": "M19","name": "เพชรบุรี","Have_Connect_Station": True,"Connect-station":"มักกะสัน","Connect-Route":"AIRPORT-LINK"},
                          {"code": "M20","name": "พระราม9", "Have_Connect_Station": False},{"code": "M21","name": "ศูนย์วัฒนธรรมฯ", "Have_Connect_Station": False},
                          {"code": "M22","name": "ห้วยขวาง", "Have_Connect_Station": False},{"code": "M23","name": "สุทธิสาร", "Have_Connect_Station": False},
                          {"code": "M24","name": "รัชดาภิเษก", "Have_Connect_Station": False},
                          {"code": "M25","name": "ลาดพร้าว", "Have_Connect_Station": False},
                          {"code": "M26","name": "พหลโยธิน","Have_Connect_Station": True,"Connect-station":"สถานีห้าแยกลาดพร้าว","Connect-Route":"BTS-SUKUMVIT"},
                          {"code": "M27","name": "สวนจตุจักร","Have_Connect_Station": True,"Connect-station":"สถานีหมอชิต","Connect-Route":"BTS-SUKUMVIT"}
                          ]
    },
}


@router.get('/get-all')
async def getAll():
    return TrainRoute_db


@router.get('/get-route-by-name')
def getRoute(name: str = None):
    for route_id in TrainRoute_db:
        if TrainRoute_db[route_id]["Route"] == name:
            return TrainRoute_db[route_id]
    return {"data" : "Not found try BTS-SUKUMVIT ,BTS-SILOM , AIRPORT-LINK, MRT"}



@router.get('/get-have-connect-station')
def getConnectSta(name: str = None):
    for route_id in TrainRoute_db:
        if TrainRoute_db[route_id]["Route"] == name:
            trueList = []
            for i in TrainRoute_db[route_id]["Train_Station"]:
                if i["Have_Connect_Station"] == True:
                    trueList.append(i)
            return trueList

    return {"data" : "Not found try BTS-SUKUMVIT ,BTS-SILOM , AIRPORT-LINK, MRT"}



@router.get('/get-have-connect-station-all')
def getConnectStaAll():
    trueList = []
    for route_id in TrainRoute_db:    
            for i in TrainRoute_db[route_id]["Train_Station"]:
                if i["Have_Connect_Station"] == True:
                    trueList.append(i)
    return trueList
