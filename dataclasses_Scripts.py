from dataclasses import dataclass
from dataclass_wizard import JSONSerializable
from datetime import datetime

@dataclass
class blog_valid(JSONSerializable):
    id:str
    name:str
    description:str
    createdBy:str
    topic:str
    blogBody:str
    isPosted:str
   
	








   
	