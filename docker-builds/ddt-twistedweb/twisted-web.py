from twisted.web.server import Site
from twisted.web.static import File
from twisted.internet import reactor, endpoints

resource = File('web')
factory = Site(resource)
endpoint = endpoints.TCP4ServerEndpoint(reactor, 80)
endpoint.listen(factory)
reactor.run()
