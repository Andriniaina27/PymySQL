from models.touriste import Touriste
from models.groupe import Groupe
import urllib.parse


class TouristeController(object):
    @staticmethod
    async def __load(send, filename, dico=None):
        with open(filename, "r", encoding="utf-8") as f:
            html = f.read()
        
        if dico:
            for key, value in dico.items():
                placeholder = "{{ " + str(key) + " }}"
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
        await __class__.__load(send, "views/dashboard.html", dics)
    

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
    async def opInsert(scope, receive, send):
        event = await receive()
        body = event.get("body", b'')
        dico = urllib.parse.parse_qs(body.decode())

        nom    = dico.get("nom", b"")
        prenom = dico.get("prenom", b"")
        age    = dico.get("age", b"")
        groupe = dico.get("groupe", b"")
        Touriste.insert(nom, prenom, age, groupe)

        await send({
            "type": "http.response.start",
            "status": 302,
            "headers": [(b"Location", b"/listTouriste")]
        })
        await send({
            "type": "http.response.body",
            "body": b""
        })
        
    
    @staticmethod
    async def touristeInsert(scope, receive, send):
        groupe = Groupe.getAll()
        options = ""

        for g in groupe:
            options += f'<option value="{g["id_groupe"]}">{g["nomG"]}</option>'
        context = {"options_groupe": options}
        await __class__.__load(send, "views/create.html", context)
    
    @staticmethod
    async def listTouriste(scope, receive, send):
        touriste = Touriste.getAllJoin(
            joins=[("groupe", "touriste.groupe_id = groupe.id_groupe")],
            colonne=[("touriste.nom", "touriste.prenom", "touriste.age", "groupe.nomG as nomGrp", "touriste.id_touriste")]
        )

        list_Touriste = ""
        for t in touriste:
            list_Touriste += f"""
                <tr>
                    <td>{t['nom']}</td>
                    <td>{t['prenom']}</td>
                    <td>{t['age']} ans</td>
                    <td>{t['nomG']}</td>
                    <td width = 200 class="action">
                        <form action="/opdelete" method="post">
                            <input type="hidden" name="id" id="" value="{t['id_touriste']}">
                            <button type="submit">Supprimer</button>
                        </form>
                        <a href='/update/{t['id_touriste']}'>Modifier</a>
                    </td>
                </tr>
            """
        context = {"table_touristes" : list_Touriste}
        await __class__.__load(send, "views/table.html", context)
    
    @staticmethod
    async def deleteTouriste(scope, receive, send):
        try:
            event = await receive()
            body = event.get("body", b'')
            dico = urllib.parse.parse_qs(body.decode())

            id    = dico.get("id", b"")
            Touriste.delete(id)

            await send({
                "type": "http.response.start",
                "status": 302,
                "headers": [(b"Location", b"/listTouriste")]
            })
            await send({
                "type": "http.response.body",
                "body": b""
            })
        except Exception as e:
            # Si une erreur arrive -> afficher un message au lieu d'un 500 silencieux
            print("Erreur suppression :", e)
            await send({
                "type": "http.response.start",
                "status": 500,
                "headers": [(b"content-type", b"text/plain; charset=utf-8")]
            })
            await send({
                "type": "http.response.body",
                "body": f"Erreur lors de la suppression : {e}".encode()
            })
    
    async def updateTouriste(scope, receive, send, id):
        id = int(id)
        liste = Touriste.getById(id)
        groupe = Groupe.getAll()
        options = ""

        for g in groupe:
            options += f'<option value="{g["id_groupe"]}">{g["nomG"]}</option>'
        
        ajout = ""
        ajout = f"""
            <div class="input">
                <label for="Nom">Nom</label>
                <input type="text" name="nom" id="" value="{liste["nom"]}">
            </div>
            <div class="input">
                <label for="Nom">Prenom</label>
                <input type="text" name="prenom" id="" value="">
            </div>
            <div class="input">
                <label for="Nom">Age</label>
                <input type="number" name="age" id="" value="">
            </div>
        """
        context = {
            "ajout" : ajout,
            "options_groupe": options
        }
        await __class__.__load(send, "views/update.html", context)
    