from dataclasses import dataclass

@dataclass
class CustomerCarRent:
    id:int
    car_id:int
    customer_id:int
    num_of_days:int
    base_price:float
    payment_type:str # pre payment or post payment