Answers with screenshots are in "Hw 3.pdf".


Hw 3


Task 1

1.
mininet> nodes
available nodes are:
c0 h1 h2 h3 h4 h5 h6 h7 h8 s1 s2 s3 s4 s5 s6 s7
mininet> net
h1 h1-eth0:s3-eth2
h2 h2-eth0:s3-eth3
h3 h3-eth0:s4-eth2
h4 h4-eth0:s4-eth3
h5 h5-eth0:s6-eth2
h6 h6-eth0:s6-eth3
h7 h7-eth0:s7-eth2
h8 h8-eth0:s7-eth3
s1 lo:  s1-eth1:s2-eth1 s1-eth2:s5-eth1
s2 lo:  s2-eth1:s1-eth1 s2-eth2:s3-eth1 s2-eth3:s4-eth1
s3 lo:  s3-eth1:s2-eth2 s3-eth2:h1-eth0 s3-eth3:h2-eth0
s4 lo:  s4-eth1:s2-eth3 s4-eth2:h3-eth0 s4-eth3:h4-eth0
s5 lo:  s5-eth1:s1-eth2 s5-eth2:s6-eth1 s5-eth3:s7-eth1
s6 lo:  s6-eth1:s5-eth2 s6-eth2:h5-eth0 s6-eth3:h6-eth0
s7 lo:  s7-eth1:s5-eth3 s7-eth2:h7-eth0 s7-eth3:h8-eth0
c0

2.
mininet> h7 ifconfig
h7-eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 10.0.0.7  netmask 255.0.0.0  broadcast 10.255.255.255
        inet6 fe80::204e:c8ff:fe1f:f0c3  prefixlen 64  scopeid 0x20<link>
        ether 22:4e:c8:1f:f0:c3  txqueuelen 1000  (Ethernet)
        RX packets 47  bytes 3750 (3.7 KB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 8  bytes 648 (648.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536
        inet 127.0.0.1  netmask 255.0.0.0
        inet6 ::1  prefixlen 128  scopeid 0x10<host>
        loop  txqueuelen 1  (Local Loopback)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0


Task 2

1.
_handle_PacketIn -> act_like_hub -> resend_packet

2.
a. h1-h2: avg = 1.490 ms | h1-h8:avg = 5.454 ms
b. h1-h2: min = 1.097 ms, max = 3.195 ms | h1-h8: min 4.723 ms, max = 44.636 ms
c. The difference is h1-h2 takes less time than h1-h8. This is because for h1-h2, packets only need to go through switch s3, but for h1-h8, packets will have to go through switches s3, s2, s1, s5, and s7 so the ping takes longer.

3.
a. “iperf” tests the maximum network bandwidth by measuring how much data can be transferred between two nodes within a given time frame. This is also known as throughput.
b. h1-h2: 8.01 Mbits/sec, h2-h1: 9.27 Mbits/sec | h1-h8: 4.63 Mbits/sec, h8-h1: 5.46 Mbits/sec
c. The throughput for h1-h2 is larger than h1-h8. As h1-h2 only needs to go through one switch, it takes the packets a shorter time to be transferred, so more packets can be transferred within a given time frame. h1-h8 will have to go through switches s3, s2, s1, s5, and s7,

4.
All of the switches observe traffic for h1-h2 and h1-h8. I put in ‘print(“PACK IN:”, self.connection)’ in the _handle_PacketIn function to see this.


Task 3

1.
The "MAC to Port" map is established by the Tutorial object for each switch storing the MAC address as key and the port as its value for the MAC addresses that are not known when a packet is received from said MAC address. This way, the switch can send packets directly to the ports it needs to send packets to if the packet destination MAC address and port is known.

2.
a. h1-h2: avg = 1.371 ms | h1-h8:avg = 4.650 ms
b. h1-h2: min = 0.951 ms, max = 1.764 ms | h1-h8: min 4.723 ms, max = 7.633 ms
c. The pings take a shorter time than in Task 2 because the switches know where to send their packets after the first packet flood. It does not have to send packets to every port and instead it can send the packets to the specific destination port.

3.
a. h1-h2: 23.0 Mbits/sec, h2-h1: 24.4 Mbits/sec | h1-h8: 3.54 Mbits/sec, h8-h1: 4.11 Mbits/sec
b. The throughput for h1-h2 is much larger as the destination port is known by the sender, so the data transfer is faster and more data can be sent within a given time frame. There is not much of a change in throughput for h1-h8. This could be because the network path still consists of five switches and the map might not have a big effect in the short “iperf” measurement time frame.
