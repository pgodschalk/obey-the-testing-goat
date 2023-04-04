# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.box = "marcinbojko/oraclelinux9_arm64"

  config.vm.network "forwarded_port", guest: 22, host: 6666, host_ip: "127.0.0.1"
  config.vm.network "forwarded_port", guest: 443, host: 8000, host_ip: "127.0.0.1"

  config.vm.provision "ansible" do |ansible|
    ansible.extra_vars = {
      host: "localhost",
      vagrant_tasks: true,
      wsgi_port: 8001
    }
    ansible.playbook = "deploy_tools/provision.ansible.yaml"
  end
  config.vm.provision "file", source: "~/.ssh/id_ed25519.pub", destination: "~/.ssh/authorized_keys"
end
