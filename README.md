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

    pip install virtualenv
    virtualenv venv
    source venv/bin/activate
    pip install –r reqs.txt (This will install all requirements for this project)
    python manage.py syncdb (create master password for your project)
    python manage.py collectstatic
    python manage.py runserver
    python -m smtpd -n -c DebuggingServer localhost:1025 (Current version needs your own email server running to authenticate/two-factor authentication)



