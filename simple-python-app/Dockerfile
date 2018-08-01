FROM devhub-docker.cisco.com/iox-docker/ir800/base-rootfs

RUN opkg update && opkg install python
COPY poll-temperature.py /usr/bin/poll-temperature.py
COPY Telnet_test_M.py /usr/bin/Telnet_test_M.py
COPY Ping_test_M.py /usr/bin/Ping_test_M.py
COPY TelnetPing_loop.py /usr/bin/TelnetPing_loop.py

RUN chmod 777 /usr/bin/poll-temperature.py
RUN chmod 777 /usr/bin/Telnet_test_M.py
RUN chmod 777 /usr/bin/Ping_test_M.py
RUN chmod 777 /usr/bin/TelnetPing_loop.py

CMD /usr/bin/TelnetPing_loop.py 172.30.102.253 172.30.102.253 cisco cisco
