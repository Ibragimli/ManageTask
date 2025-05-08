from dataclasses import dataclass


@dataclass()
class Task:
    id:int
    title:str
    description:str
    completed:bool

# # Domain/Entities/Task.py
# class Task:
#     def __init__(self, id: int, title: str, description: str):
#         self.id = id
#         self.title = title
#         self.description = description
