import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_vm_guest_package(host):
    pkg1 = host.package('open-vm-tools')
    pkg2 = host.package('qemu-guest-agent')

    assert pkg1.is_installed
    assert pkg2.is_installed
