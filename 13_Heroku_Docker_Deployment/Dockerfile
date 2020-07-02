#Dockerfile to run Python
FROM ubuntu:18.04

#adding env variables from host
#ARG fake_user=none
#ENV falseuser=$fake_user

#copying directories in from host
COPY TDirectory /TDirectory

#pulling various useful packages
RUN apt-get -y update \
&& apt-get -y upgrade python3 \
&& apt install -y python3-pip \
&& apt install -y python3-venv \
&& apt-get -y install cron \
&& apt install -y vim

#installing python virtualenv package and a few other important pieces.
RUN python3 -m pip install --user virtualenv 
RUN python3 -m venv mavenv 
RUN pip3 install -r /TDirectory/requirements.txt
RUN python3 -m ipykernel install --user --name=mavenv

#changing permissioning on scripts to be run
RUN chmod +x /TDirectory/Shellscript.sh


#crontab setup from mycron file
#ADD mycron /etc/cron.d/mycron
#RUN chmod 0644 /etc/cron.d/mycron
#RUN crontab /etc/cron.d/mycron
#CMD env > etc/environment && cron -f


#-------------------------






































#drop ENV LC_ALL=C.UTF-8
#drop ENV LANG=C.UTF-8

#drop WORKDIR /MavenAlerts

# VOLUME /MavenAlerts/Output



#CMD service cron restart

#RUN ["/bin/bash/" , "-c", "source /MavenAlerts/mavenv/bin/activate"]

#RUN /MavenAlerts/MavenAlertsNoJT.sh
#VOLUME /MavenAlerts/output
#RUN service cron restart

#~~~~~~~~~~~~~~~~~~~~~~~~~~

#RUN export LC_ALL=C.UTF-8 \
#&& export LANG=C.UTF-8 


#&& /etc/init.d/cron start \
#&& echo "*/2 * * * * /MavenAlerts/MavenAlertsNoJT.sh" >> mycron \
#&& crontab mycron 
#&& chmod 0644 /etc/cron.d/hello
#&& /etc/init.d/cron reload
#&& crontab -l | { cat; echo "*/2 * * * * /MavenAlerts/MavenAlertsNoJT.sh"; } | crontab -
#crontab -e 



#RUN echo $mavenuser && echo $mavenpw && echo $emailuser && echo $emailpw
#CMD cron && tail -f /var/log/cron.log



#RUN source mavenv/bin/activate 
#RUN pip3 install -r /MavenAlerts/requirements.txt 
#RUN chmod +x /MavenAlerts/MavenAlertsNoJT.sh 
#RUN /MavenAlerts/MavenAlertsNoJT.sh


#after venv is installed have to...
#1. Make new environment
#2. Would have to install everything into venv
#3. activate the virtual environment
#
#will have to apt install cron
#apt install cron (?)
#Make sure that MavenAlerts.sh is executable
#After cron is installed will have to make a script
#which would go something like this
# 30 09 * * 1-5 /usr/local/bin/MavenAlertsTest/MavenAlerts.sh
#
#Will want to test cron job locally first, but after it is
#set up will want to go ahead and copy the crontab setup
#process into this container
#
#Have to make sure that jupyter/ipython are installed
#as well as a few other main libraries.
# NOTE: best practice for venv will be to make something
#on the virtual ubuntu box and then try to port it out to
#my local (?)
#
#Because MavenAlerts.sh just kicks off other things
#will be able to leave it at that and it should work properly
#so long as making connections out from the box isn't
#much of a problem.
