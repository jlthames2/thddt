import subprocess
import random
import time
import sys


class DynamicDocker(object):
    '''Class used to create dynamic deception with containers and Docker'''

    def __init__(self):
        self.containers = ['jlthames2/thddt-web',
                           'jlthames2/thddt-pymodbus',
                           'jlthames2/thddt-pubsub',
                           'jlthames2/thddt-echo']

        self.numContainers = 10
        self.uniqueContainers = len(self.containers)
        self.sleepTime = 10
        self.portLow = 1000
        self.portHigh = 20000


    def dockerRun(self):
        '''Run the containers.'''
        for x in xrange(0, self.numContainers):
            index = random.randrange(0, self.uniqueContainers)
            container = self.containers[index]
            port = random.randrange(self.portLow,self.portHigh)
            command = 'docker run -d -p%s:80 %s' % (port, container)

            print "Starting docker %s process on port %s" % (container, port)
            p = subprocess.Popen(command, shell=True)
            p.wait()


    def dockerStop(self):
        '''Stop and remove running containers.'''
        p = subprocess.Popen('docker stop $(docker ps -aq)', shell=True)
        p.wait()
        p = subprocess.Popen('docker rm $(docker ps -aq)', shell=True)
        p.wait()


    def run(self):
        '''Endlessly call dockerRun and dockerStop to create random
           containers on random ports.'''

        try:

            while(True):
                self.dockerRun()
                time.sleep(self.sleepTime)
                self.dockerStop()

        except KeyboardInterrupt:
            print "Interrupt caught. Cleaning up and stopping..."
            self.dockerStop()
            sys.exit(0)




if __name__ == '__main__':
    dynDocker = DynamicDocker()
    dynDocker.run()
