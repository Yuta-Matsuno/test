FROM devhub-docker.cisco.com/iox-docker/ir800/base-rootfs

RUN opkg update && opkg install python
COPY poll-temperature.py /usr/bin/poll-temperature.py
COPY Telnet_test_M.py /usr/bin/Telnet_test_M.py
COPY Ping_test_M.py /usr/bin/Ping_test_M.py
COPY TelnetPing_loop.py /usr/bin/TelnetPing_loop.py
COPY datetime.py /usr/bin/datetime.py
COPY telnetlib.py /usr/bin/telnetlib.py
COPY abc.py /usr/bin/abc.py
COPY enum.py /usr/bin/enum.py
COPY io.py /usr/bin/io.py
COPY os.py /usr/bin/os.py
COPY selectors.py /usr/bin/selectors.py
COPY socket.py /usr/bin/socket.py
COPY stat.py /usr/bin/stat.py
COPY execshell.py /usr/bin/execshell.py
COPY telnet.sh /usr/bin/telnet.sh
COPY shell.sh /usr/bin/shell.sh

RUN chmod 777 /usr/bin/datetime.py
RUN chmod 777 /usr/bin/poll-temperature.py
RUN chmod 777 /usr/bin/Telnet_test_M.py
RUN chmod 777 /usr/bin/Ping_test_M.py
RUN chmod 777 /usr/bin/TelnetPing_loop.py
RUN chmod 777 /usr/bin/telnetlib.py
RUN chmod 777 /usr/bin/abc.py
RUN chmod 777 /usr/bin/enum.py
RUN chmod 777 /usr/bin/io.py
RUN chmod 777 /usr/bin/os.py
RUN chmod 777 /usr/bin/selectors.py
RUN chmod 777 /usr/bin/socket.py
RUN chmod 777 /usr/bin/stat.py
RUN chmod 777 /usr/bin/execshell.py
RUN chmod 777 /usr/bin/telnet.sh
RUN chmod 777 /usr/bin/shell.sh
