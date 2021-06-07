FROM centos
RUN yum update -y && \
    yum install httpd -y && \
    yum install httpd-tools -y
RUN yum -y install \
    php \
    php-cli\
    php-common

RUN echo "<?php phpinfo(); ?>" > /var/www/html/info.php

EXPOSE  80

CMD apachectl -DFOREGROUND
