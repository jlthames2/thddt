from twisted.internet import protocol, reactor, endpoints

class Echo(protocol.Protocol):
    def dataReceived(self, data):
        self.transport.write(data)

class EchoFactory(protocol.Factory):
    def buildProtocol(self, addr):
        return Echo()


endpoint = endpoints.TCP4ServerEndpoint(reactor, 80)
endpoint.listen(EchoFactory())
reactor.run()
