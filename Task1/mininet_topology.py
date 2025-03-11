from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import Controller
from mininet.cli import CLI
from mininet.link import TCLink

class CustomTopo(Topo):
    def build(self):
        h1 = self.addHost('h1')
        h2 = self.addHost('h2')
        h3 = self.addHost('h3')
        h4 = self.addHost('h4')
        h5 = self.addHost('h5')
        h6 = self.addHost('h6')
        h7 = self.addHost('h7')
        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')
        s3 = self.addSwitch('s3')
        s4 = self.addSwitch('s4')

        self.addLink(h1, s1, bw=100)
        self.addLink(h2, s1, bw=100)
        self.addLink(h3, s2, bw=50)
        self.addLink(h4, s2, bw=50)
        self.addLink(h5, s3, bw=100)
        self.addLink(h6, s3, bw=100)
if _name_ == '_main_':
    topo = CustomTopo()
    net = Mininet(topo=topo, controller=Controller, link=TCLink)
    net.start()
    CLI(net)
    net.stop()