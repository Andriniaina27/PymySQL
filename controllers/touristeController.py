from models.touriste import Touriste


class TouristeController(object):
    @staticmethod
    async def __load(send, filename, dico=None):
        with open(filename, "r", encoding="utf-8") as f:
            html = f.read()
        
        if dico:
            for key, value in dico.items():
                placeholder = "{{ " + str(key) + "}}"
                html = html.replace(placeholder, str(value))
        
        await send({
            'type' : 'http.response.start',
            'status' : 200,
            'headers' : [(b'content-type', b'text/html')]
        })

        await send({
            'type' : 'http.response.body',
            'body' : html.encode()
        })
    @staticmethod
    async def index(scope, receive, send):
        last = Touriste.lastId() + 1
        dics = {"numero" : last}
        await __class__.__load(send, "views/index.html", dics)
    

    @staticmethod
    async def error404(scope, receive, send):
        await __class__.__load(send, "views/error404.html")
        # assert scope['type'] == 'http'

        # with open("views/error404.html", "r", encoding="utf-8") as f:
        #     html = f.read()
        
        # await send({
        #     'type' : 'http.response.start',
        #     'status' : 200,
        #     'headers' : [(b'content-type', b'text/html')]
        # })

        # await send({
        #     'type' : 'http.response.body',
        #     'body' : html.encode()
        # })
    
    @staticmethod
    async def opInsert():
        pass
    