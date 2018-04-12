FROM jenkins/jenkins:lts

USER root
RUN apt-get update -y
RUN apt-get install python3 sudo -y
RUN update-alternatives --install /usr/bin/python python /usr/bin/python3 0
RUN usermod -G sudo jenkins
RUN echo 'jenkins   ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers
ARG user=jenkins
ARG group=jenkins
ARG uid=1000
ARG gid=1000
ARG http_port=8080
ARG agent_port=50000


# Installing Golang
RUN cd /tmp; wget https://dl.google.com/go/go1.10.linux-amd64.tar.gz && \
    tar -C /usr/local -zxvf go1.10.linux-amd64.tar.gz && \
    export PATH=$PATH:/usr/local/go/bin
#### Terraform  ###############
RUN cd /tmp
RUN cd /tmp && wget https://releases.hashicorp.com/terraform/0.11.3/terraform_0.11.3_linux_amd64.zip
RUN cd /tmp && mv terraform_0.11.3_linux_amd64.zip terraform_install.zip && unzip terraform_install.zip -d /usr/local/bin/
RUN terraform version

RUN mkdir -p /root/terraform/env_vars && mkdir /root/terraform/environments
USER ${user}
#COPY ["read_credentials.py", "/opt/read_credentials.py"]
ENTRYPOINT ["/sbin/tini", "--", "/usr/local/bin/jenkins.sh"]
