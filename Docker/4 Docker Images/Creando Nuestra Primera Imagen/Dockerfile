FROM centos

LABEL version=1.0
LABEL description="This is apache image"
LABEL Vendor="yo"

RUN yum install httpd -y

#COPY startbootstrap-freelancer-master /var/www/html

RUN echo "$(whoami)" > /var/www/html/user1.html

RUN useradd ricardo

USER ricardo

RUN echo "$(whoami)" > /tmp/user2.html

USER root

RUN cp /tmp/user2.html /var/www/html/user2.html

COPY run.sh /run.sh

CMD sh /run.sh
