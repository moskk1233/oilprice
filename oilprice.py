import requests
import datetime
import json
from prettytable import PrettyTable

OIL_TYPES = {
    1: "Super Power Diesel",
    7: "Bensin",
    9: "Gasohol 95",
    10: "Gasohol 91",
    11: "Gasohol E20",
    12: "Gasohol E85",
    17: "Diesel",
    22: "Super Power Gasohol 95",
}


PROVINCES = {
    1: "Bangkok",
    2: "Samut Prakan",
    3: "Nonthaburi",
    4: "Pathum Thani",
    5: "Ayutthaya",
    6: "Ang Thong",
    7: "Lop Buri",
    8: "Sing Buri",
    9: "Chai Nat",
    10: "Saraburi",
    11: "Chon Buri",
    12: "Rayong",
    13: "Chanthaburi",
    14: "Trat",
    15: "Chachoengsao",
    16: "Prachin Buri",
    17: "Nakhon Nayok",
    18: "Sa Kaeo",
    19: "Nakhon Ratchasima",
    20: "Buri Ram",
    21: "Surin",
    22: "Si Sa Ket",
    23: "Ubon Ratchathani",
    24: "Yasothon",
    25: "Chaiyaphum",
    26: "Amnat Charoen",
    27: "Nong Bua Lamphu",
    28: "Khon Kaen",
    29: "Udon Thani",
    30: "Loei",
    31: "Nong Khai",
    32: "Maha Sarakham",
    33: "Roi Et",
    34: "Kalasin",
    35: "Sakon Nakhon",
    36: "Nakhon Phanom",
    37: "Mukdahan",
    38: "Chiang Mai",
    39: "Lamphun",
    40: "Lampang",
    41: "Uttaradit",
    42: "Phrae",
    43: "Nan",
    44: "Phayao",
    45: "Chiang Rai",
    46: "Mae Hong Son",
    47: "Nakhon Sawan",
    48: "Uthai Thani",
    49: "Kamphaeng Phet",
    50: "Tak",
    51: "Sukhothai",
    52: "Phitsanulok",
    53: "Phichit",
    54: "Phetchabun",
    55: "Ratchaburi",
    56: "Kanchanaburi",
    57: "Suphan Buri",
    58: "Nakhon Pathom",
    59: "Samut Sakhon",
    60: "Samut Songkhram",
    61: "Phetchaburi",
    62: "Prachuap Khiri Khan",
    63: "Nakhon Si Thammarat",
    64: "Krabi",
    65: "Phang Nga",
    66: "Phuket",
    67: "Surat Thani",
    68: "Ranong",
    69: "Chumphon",
    70: "Songkhla",
    71: "Satun",
    72: "Trang",
    73: "Phatthalung",
    74: "Pattani",
    75: "Yala",
    76: "Narathiwat",
    77: "Bueng Kan",
}

def send_request(month: int, year: int):
    headers = {
        "Content-Type": "application/json",
        "Accept": "*/*"
    }

    payload = {
        "provinceId": 1,
        "month": month,
        "year": year,
        "pageSize": 10000,
        "pageIndex": 0
    }
    response = requests.post(
        "https://orapiweb1.pttor.com/api/oilprice/search",
        json=payload,
        headers=headers
    )

    return response

def show_oil(data: dict) -> None:
    for item in data["data"]:
        for oil_data in json.loads(item["priceData"]):
            oil_type_id = oil_data["OilTypeId"]
            oil_price = oil_data["Price"]
            oil_date = oil_data["PriceDate"]

            oil_name = OIL_TYPES.get(oil_type_id, "Unknown Oil")
            oil_date = datetime.datetime.strptime(oil_date, "%Y-%m-%dT%H:%M:%S")
            oil_date = oil_date.strftime("%d-%m-%Y %H:%M:%S")

            table.add_row([oil_name, f"{oil_price} ฿", oil_date])

    print(table)


if __name__ == "__main__":
    table = PrettyTable(
        ['Name', 'Price', 'Date'], 
        title='Oil Price'
    )
    
    today = datetime.date.today()
    data = send_request(today.month, today.year).json()
    show_oil(data)
    print("Press enter key to continue...")
    input()