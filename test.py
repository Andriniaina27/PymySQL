# from models.touriste import Touriste
# from controllers.touristeController import TouristeController

# tour = TouristeController()

# print(tour.deleteTouriste(id))
print("Bonjour")
from models.touriste import Touriste
class Tour(object):
    @staticmethod
    async def deleteTouriste(scope, receive, send, id=4):
        print("ID reçu :", id)
        id = int(id)   # conversion
        # print(f"Valeur id : {id} ")
        # Touriste.delete(id)  # suppression en BDD

        # await send({
        #     "type": "http.response.start",
        #     "status": 302,
        #     "headers": [(b"Location", b"/listTouriste")]
        # })
        # await send({
        #     "type": "http.response.body",
        #     "body": b""
        # })