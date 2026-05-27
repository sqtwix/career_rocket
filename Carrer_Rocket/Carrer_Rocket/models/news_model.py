from datetime import date
from dataclasses import dataclass

@dataclass
class NewsModel():
    header : str
    description : str
    author : str
    postDate : date
    text : str