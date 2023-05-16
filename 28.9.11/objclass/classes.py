from pydantic import BaseModel, Field
import datetime as datetime

class AuthRequest(BaseModel):
    username: str = Field(...)
    password: str = Field(...)

class TokenResponse(BaseModel):
    token: str = Field(...)

class BookingDates(BaseModel):
    checkin: datetime.date = Field(...)
    chechout: datetime.date = Field(...)


class Booking(BaseModel):
    firstname: str = Field(...)
    lastname: str = Field(...)
    totalprice: str = Field(...)
    depositpaid: bool = Field(...)
    bookingdates: dict = Field(...)
    additionalneeds: str = Field(...)

class BookingResponse(BaseModel):
    bookingid: int
    booking: Booking

class CheckinChechout(BaseModel):
    bookingdates: BookingDates


