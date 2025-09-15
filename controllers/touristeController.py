class Touriste(object):
    @staticmethod
    async def index(scope, receive, send):
        assert scope['type'] == 'http'

        with open("views/index.html", "r", encoding="utf-8") as f:
            html = f.read()
        
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
    async def pageInsert(scope, receive, send):
        assert scope['type'] == 'http'

        with open("views/insert.html", "r", encoding="utf-8") as f:
            html = f.read()
        
        await send({
            'type' : 'http.response.start',
            'status' : 200,
            'headers' : [(b'content-type', b'text/html')]
        })

        await send({
            'type' : 'http.response.body',
            'body' : html.encode()
        })
    