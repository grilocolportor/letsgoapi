import falcon

from user.persistence.crud import Crud

api = falcon.API()
qall = Crud()

api.add_route("/user/persistence/", qall)