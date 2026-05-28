from datetime import date
from dataclasses import dataclass

@dataclass
class ArticleModel():
    header: str
    description: str
    author: str
    authorMail: str
    postDate: date
    text: str