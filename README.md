clinicv2
========

Clinicv2 - Second update on NoteTaker Application developed in Django

Components in the system
========================
Django based
Browser only
Single page note-taker app, that has has a text-area with autocomplete options.
Two-factor authentication
Connected to default HSQLDB (default)

Previous Version
================

Clinic-1.0 – 
https://github.com/valllichidambaram/clinic.1.0/

Project Directories
===================

Directory Structure
  Clinic.1.0
    Added reqs.txt
    Few major changes in Static

Installing Development Environment
==================================


Create virtual env.

    pip install virtualenv
    virtualenv venv
    source venv/bin/activate

Install Dependcies

    pip install –r reqs.txt 

Set master password

    python manage.py syncdb 


    python manage.py collectstatic
    python manage.py runserver

    
Email server needed for two factor Auth

    python -m smtpd -n -c DebuggingServer localhost:1025 



