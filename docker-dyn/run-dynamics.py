import subprocess
import random
import time
import sys


class DynamicDocker(object):
    '''Class used to create dynamic deception with containers and Docker'''

    def __init__(self):
        self.containers = ['jlthames2/thddt-web', 'jlthames2/thddt-pymodbus']
        self.numContainers = 3
        #sleep 10 seconds before respawning
        self.sleepTime = 10
        self.portLow = 1000
        self.portHigh = 2000


    def dockerRun(self):
        '''Run the containers.'''
        for x in xrange(0, self.numContainers):
            index = random.randrange(0,2)
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
        while(True):
            try:
                self.dockerRun()
                time.sleep(self.sleepTime)
                self.dockerStop()
            except KeyboardInterrupt:
                print "Interrupt caught. Cleaning up and stopping..."
            finally:
                # clean up
                self.dockerStop()
                sys.exit(0)



if __name__ == '__main__':
    dynDocker = DynamicDocker()
    dynDocker.run()
