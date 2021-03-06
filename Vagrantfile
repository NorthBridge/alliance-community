# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  # Every Vagrant development environment requires a box. You can search for
  # boxes at https://atlas.hashicorp.com/search.
  config.vm.box = 'ubuntu/trusty32'

  # Create a forwarded port mapping which allows access to a specific port
  # within the machine from a port on the host machine. In the example below,
  # accessing "localhost:8000" will access port 8080 on the guest machine.
  config.vm.network :forwarded_port, guest: 8001, host: 8081
  config.vm.network :forwarded_port, guest: 9001, host: 9091

  # Share an additional folder to the guest VM. The first argument is
  # the path on the host to the actual folder. The second argument is
  # the path on the guest to mount the folder. And the optional third
  # argument is a set of non-required options.
  # config.vm.synced_folder "../data", "/vagrant_data"
  # config.vm.synced_folder '.', '/home/vagrant/'
  
  config.vm.provision "file", source: "../alliance-community/alliance/config/.bash_aliases", destination: ".bash_aliases"
  config.vm.provision "file", source: "../alliance-community/logs/alliance_template.log", destination: "/vagrant/alliance/logs/alliance.log"

  # Enable provisioning with a shell script. Additional provisioners such as
  # Puppet, Chef, Ansible, Salt, and Docker are also available. Please see the
  # documentation for more information about their specific syntax and use.
  config.vm.provision 'shell', inline: <<-SHELL
  
  	if [ ! -e "/vagrant/alliance/config/local_settings.py" ]; then
       echo "================================================================================"
       echo "Copying local settings template to local system"
       echo "================================================================================"
       cp /vagrant/alliance/config/local_settings_template.py /vagrant/alliance/config/local_settings.py
    else
       echo "================================================================================"
       echo "Local settings file already found. Not overwriting."
       echo "================================================================================"
    fi
  
    echo "================================================================================"
    echo "Getting package updates"
    echo "================================================================================"
    sudo apt-get update


    echo "================================================================================"
    echo "Installing python2.7 python-dev postgresql-9.3 libpq-dev python-pip virtualenvwrapper"
    echo "================================================================================"
    sudo apt-get install -y apache2 python2.7 python-dev postgresql-9.3 libpq-dev python-pip virtualenvwrapper

    echo "================================================================================"
    echo "Creating a superuser for the database."
    echo "================================================================================"
    sudo -u postgres psql -c "CREATE USER alliance WITH PASSWORD 'beloved';"
    sudo -u postgres psql -c "ALTER USER alliance WITH superuser;"
    echo "================================================================================"
    echo "Creating database and inserting static data, triggers."
    echo "================================================================================"
    sudo -u postgres psql -c "CREATE DATABASE northbr6_devwaterwheel;"
    sudo -u postgres psql northbr6_devwaterwheel < /vagrant/bin/seed/static_inserts.sql
    sudo -u postgres psql northbr6_devwaterwheel < /vagrant/bin/seed/postgres_update_trigger.sql

    echo "================================================================================"
    echo "Creating a virtualenv and installing requirements"
    echo "================================================================================"
    mkvirtualenv alliance
    workon alliance
    cd /vagrant
    pip install -r requirements.txt
  SHELL
end
