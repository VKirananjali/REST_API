from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

FULL_NAME = "vemula_kirananjali"
DOB = "19022005"
EMAIL = "kirananjali.22bce9547@vitapstudent.ac.in"
ROLL_NUMBER = "22BCE9547"

class InputData(BaseModel):
    data: List[str]

@app.post("/bfhl")
async def bfhl_endpoint(payload: InputData):
    try:
        data = payload.data

        even_numbers = []
        odd_numbers = []
        alphabets = []
        special_characters = []
        num_sum = 0
        concat_letters = []

        for item in data:
            if item.isdigit():
                if int(item) % 2 == 0:
                    even_numbers.append(item)
                else:
                    odd_numbers.append(item)
                num_sum += int(item)
            elif item.isalpha():
                alphabets.append(item.upper())
                concat_letters.append(item)
            else:
                special_characters.append(item)

        reversed_concat = ''.join(concat_letters)[::-1]
        alt_caps = ''
        for idx, char in enumerate(reversed_concat):
            alt_caps += char.upper() if idx % 2 == 0 else char.lower()

        response = {
            "is_success": True,
            "user_id": f"{FULL_NAME}_{DOB}",
            "email": EMAIL,
            "roll_number": ROLL_NUMBER,
            "odd_numbers": odd_numbers,
            "even_numbers": even_numbers,
            "alphabets": alphabets,
            "special_characters": special_characters,
            "sum": str(num_sum),
            "concat_string": alt_caps
        }

        return response

    except Exception as e:
        return {
            "is_success": False,
            "message": "An error occurred",
            "error": str(e)
        }
