from controllers.touristeController import Touriste


router  = {
    "/" : Touriste.index,
    "/insert" : Touriste.pageInsert
}