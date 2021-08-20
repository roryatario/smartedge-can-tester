# smartedge-can-tester
Python3 CAN tester scripts for SmartEdge

Tests for behaviour reported in [1], in which about 0.1% of CAN packets are corrupted in a particular way.

To run this you'll need two SmartEdges, connected via CAN.  The CAN interfaces must be up.  Behaviour has been observed at 125kbps and 500kbps.

On both SmartEdges, install the python3-can library: `sudo apt install python3-can`

One on SmartEdge, run the sender: `python3 sendsimple.py`.  If you get "buffer full" errors, increase the transmit queue length: `ip link set can0 txqueuelen 50` .

One the other SmartEdge, run the receiver: `python3 recvsimple.py`

recvsimple.py will print out statistics once a second; these statistics are:

```
  <number-of-packets-received>   <number-of-bad-packets>   <number-of-bad-packets-matching-pattern>
```

[1] https://www.element14.com/community/message/304055/l/re-help-encountering-can-bus-problem-on-smartedge-iiot-gateway
