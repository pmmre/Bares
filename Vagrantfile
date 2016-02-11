# -*- mode: ruby -*- vi: set ft=ruby : All Vagrant configuration is done below. The "2" in Vagrant.configure configures the 
# configuration version (we support older styles for backwards compatibility). Please don't change it unless you know what you're doing.
Vagrant.configure('2') do |config|
  # The most common configuration options are documented and commented below. For a complete reference, please see the online 
  # documentation at https://docs.vagrantup.com. Every Vagrant development environment requires a box. You can search for boxes at 
  # https://atlas.hashicorp.com/search.
  config.vm.box = 'azure'
  config.vm.network "public_network"
  config.vm.network "private_network",ip: "192.168.56.11", virtualbox__intnet: "vboxnet0"
  config.vm.network "forwarded_port", guest: 80, host: 80
  config.vm.define "localhost" do |l|
          l.vm.hostname = "localhost"
   end
  config.vm.provider :azure do |azure, override|
      azure.mgmt_certificate = File.expand_path('/home/pmmre/despliegueEnAzure/azurevagrant.pem')
      azure.mgmt_endpoint = 'https://management.core.windows.net'
      azure.subscription_id = '4d42604e-09f5-4a86-bc6f-9efebe6bbe5f'
      azure.vm_image = 'b39f27a8b8c64d52b05eac6a62ebad85__Ubuntu-14_04_2-LTS-amd64-server-20150506-en-us-30GB'
      azure.vm_name = 'Bares'
      azure.vm_password = 'Clave#Pablo#1'
      azure.vm_location = 'Central US'
      azure.ssh_port = '22'
      azure.tcp_endpoints = '80:80'
  end
  config.vm.provision "ansible" do |ansible|
      ansible.sudo = true
        ansible.playbook = "bares.yml"
        ansible.verbose = "v"
        ansible.host_key_checking = false
  end
end
