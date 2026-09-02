from ninja import NinjaAPI, Schema

api = NinjaAPI()


class MessageSchema(Schema):
    name: str
    message: str


@api.get("/hello")
def hello(request):
    return {"message": "Hello from Django Ninja"}


@api.post("/message")
def create_message(request, payload: MessageSchema):
    return {
        "success": True,
        "name": payload.name,
        "message": payload.message,
    }
