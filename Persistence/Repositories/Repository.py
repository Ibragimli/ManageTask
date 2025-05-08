from Application.Repositories import  IRepository
from Domain.Entities.Task import Task
import  sqlite3

class Repository(IRepository):
    def __init__(self):
        self.database = sqlite3.connect("../Persistence/Database/Database.db")
        self.cursor = self.database.cursor()

    def Get(self, id):
        self.cursor.execute("SELECT * FROM task WHERE id = ?", (id,))
        getTask = self.cursor.fetchone()
        if getTask:
            return Task(id=getTask[0], title=getTask[1], description=getTask[2], completed=getTask[3])
        return None

    def GetAll(self):
        self.cursor.execute("SELECT * FROM task")
        getTasks = self.cursor.fetchall()
        tasks =[]
        if getTasks:
            for task in getTasks:
                tasks.append(Task(id=task[0], title=task[1], description=task[2], completed=task[3]))
            return tasks
        return None
    def Create(self,task:Task):
        self.cursor.execute("Insert into task (title,description,completed) values (?,?,?)",
                            (task.title, task.description, int(0)))
        self.database.commit()
    def Update(self,task:Task):
        self.cursor.execute("UPDATE task SET title = ?, description = ? ,completed = ? WHERE id = ?",
                            (task.title, task.description,task.completed, task.id))
        self.database.commit()
    def Delete(self,id):
        self.cursor.execute("DELETE FROM task WHERE id = ?",
                            (id,))
        self.database.commit()

    def __del__(self):
        self.cursor.close()
        self.database.close()
