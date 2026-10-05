"""" it used in dict to get specific  data  in a format """
from typing import TypedDict
from typeguard import typechecked
from typing_extensions import Required, NotRequired
import json

@typechecked
class tester(TypedDict):
    name : str
    age : Required[int]
    email : NotRequired[str]

info : tester= {
    "name" : "mohan",
    "age" : 18,
    "email" : "mohan@123"
}

info2 : tester= {
    "name" : "mohan",


}