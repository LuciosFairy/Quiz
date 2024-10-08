from http.client import responses

from requests import request, get
from Question import Question
from settings import settings


class ApiHandler:
    BASE_URL = settings["BASE_URL"]+settings["VERSION"]+"/"
    HEADERS = {
        'X-Api-Key': settings["KEY"],
        'User-Agent': 'Safari/537.36'
    }

    @staticmethod
    def getCategories() -> [str]:
        response = request("GET", ApiHandler.BASE_URL+"categories/", headers=ApiHandler.HEADERS)
        response = response.json()
        categories = [c["name"] for c in response]
        return categories


    @staticmethod
    def getQuestions(category: str, limit:int) -> [Question]:

        params = {"limit": limit}
        if category is not None:
             params["category"] = category

        url = ApiHandler.BASE_URL+"questions"
        response = get(url, headers=ApiHandler.HEADERS, params=params)

        response = response.json()
        questions = []
        for element in response:
            q = Question()
            q.question_text = element["question"]
            for value in element["answers"].values():
                if value is None:
                    break
                q.answers.append(value)
            if element['multiple_correct_answers'] == "true":
                continue

            for i, value in enumerate(element['correct_answers'].values()):
                if value == "true":
                    q.correct_answer = i
                    break
            questions.append(q)
        return questions

