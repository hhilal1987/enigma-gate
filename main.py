from fastapi import FastAPI
from pydantic import BaseModel
import os

app = FastAPI()

class UserInput(BaseModel):
    text_entity: str

class EnigmaGateApp:
    def __init__(self):
        self.actions = ["دمج", "امتصاص", "تحديث", "رفع", "إرجاء", "رفض"]

    def process_entity(self, new_entity):
        action = self.actions[3] if "أولوية" in new_entity else self.actions[0]
        return {
            "status": "تم العبور",
            "action_taken": action,
            "supervisor": "Skill Shifter",
            "directive": f"يتم الآن {action} الكيان ضمن طبقات المنظومة."
        }

enigma = EnigmaGateApp()

@app.get("/")
def read_root():
    return {"message": "Enigma Gate is Online"}

@app.post("/pulse")
def run_diagnostic(user_input: UserInput):
    result = enigma.process_entity(user_input.text_entity)
    return result
