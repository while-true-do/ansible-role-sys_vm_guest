<!--
name: README.md
description: This file contains important information for the repository.
author: while-true-do.io
contact: hello@while-true-do.io
license: BSD-3-Clause
-->

<!-- github shields -->
[![Github (tag)](https://img.shields.io/github/tag/while-true-do/ansible-role-sys_vm_guest.svg)](https://github.com/while-true-do/ansible-role-sys_vm_guest/tags)
[![Github (license)](https://img.shields.io/github/license/while-true-do/ansible-role-sys_vm_guest.svg)](https://github.com/while-true-do/ansible-role-sys_vm_guest/blob/master/LICENSE)
[![Github (issues)](https://img.shields.io/github/issues/while-true-do/ansible-role-sys_vm_guest.svg)](https://github.com/while-true-do/ansible-role-sys_vm_guest/issues)
[![Github (pull requests)](https://img.shields.io/github/issues-pr/while-true-do/ansible-role-sys_vm_guest.svg)](https://github.com/while-true-do/ansible-role-sys_vm_guest/pulls)
<!-- travis shields -->
[![Travis (com)](https://img.shields.io/travis/com/while-true-do/ansible-role-sys_vm_guest.svg)](https://travis-ci.com/while-true-do/ansible-role-sys_vm_guest)
<!-- ansible shields -->
[![Ansible (min. version)](https://img.shields.io/badge/dynamic/yaml.svg?label=Min.%20Ansible%20Version&url=https%3A%2F%2Fraw.githubusercontent.com%2Fwhile-true-do%2Fansible-role-sys_vm_guest%2Fmaster%2Fmeta%2Fmain.yml&query=%24.galaxy_info.min_ansible_version&colorB=black)](https://galaxy.ansible.com/while_true_do/sys_vm_guest)
[![Ansible (platforms)](https://img.shields.io/badge/dynamic/yaml.svg?label=Supported%20OS&url=https%3A%2F%2Fraw.githubusercontent.com%2Fwhile-true-do%2Fansible-role-sys_vm_guest%2Fmaster%2Fmeta%2Fmain.yml&query=galaxy_info.platforms%5B*%5D.name&colorB=black)](https://galaxy.ansible.com/while_true_do/sys_vm_guest)
[![Ansible (tags)](https://img.shields.io/badge/dynamic/yaml.svg?label=Galaxy%20Tags&url=https%3A%2F%2Fraw.githubusercontent.com%2Fwhile-true-do%2Fansible-role-sys_vm_guest%2Fmaster%2Fmeta%2Fmain.yml&query=%24.galaxy_info.galaxy_tags%5B*%5D&colorB=black)](https://galaxy.ansible.com/while_true_do/sys_vm_guest)

# Ansible Role: sys_vm_guest

An Ansible Role to install VM Guest Packages.

## Motivation

Virtualization is very common these days and often requires some special
packages in the guest OS.

## Description

This role installs vm guest packages.

-   detect Virtualization (KVM, VMware)
-   add proper packages

## Requirements

Used Modules:

-   [Ansible Package Module](https://docs.ansible.com/ansible/latest/modules/package_module.html)
-   [Ansible debug Module](https://docs.ansible.com/ansible/latest/modules/debug_module.html)
-   [Ansible include_vars Module](https://docs.ansible.com/ansible/latest/modules/include_vars_module.html)

## Installation

Install from [Ansible Galaxy](https://galaxy.ansible.com/while_true_do/sys_vm_guest)
```
ansible-galaxy install while_true_do.sys_vm_guest
```

Install from [Github](https://github.com/while-true-do/ansible-role-sys_vm_guest)
```
git clone https://github.com/while-true-do/ansible-role-sys_vm_guest.git while_true_do.sys_vm_guest
```

## Usage

### Role Variables

```
---
# defaults file for while_true_do.sys_vm_guest

## Package Management
wtd_sys_vm_guest_package:
  - qemu-guest-agent
  - open-vm-tools
# State can be present|latest|absent
wtd_sys_vm_guest_package_state: "present"
```

### Example Playbook

Running Ansible
[Roles](https://docs.ansible.com/ansible/latest/user_guide/playbooks_reuse_roles.html)
can be done in a
[playbook](https://docs.ansible.com/ansible/latest/user_guide/playbooks_intro.html).

#### Simple

```
---
- hosts: all
  roles:
    - role: while_true_do.sys_vm_guest
```

## Known Issues

1.  RedHat Testing is currently not possible in public, due to limitations
    in subscriptions.
2.  Some services and features cannot be tested properly, due to limitations
    in docker.

## Testing

Most of the "generic" tests are located in the
[Test Library](https://github.com/while-true-do/test-library).

Ansible specific testing is done with
[Molecule](https://molecule.readthedocs.io/en/stable/).

Infrastructure testing is done with
[testinfra](https://testinfra.readthedocs.io/en/stable/).

Automated testing is done with [Travis CI](https://travis-ci.com/while-true-do).

## Contribute

Thank you so much for considering to contribute. We are very happy, when somebody
is joining the hard work. Please fell free to open
[Bugs, Feature Requests](https://github.com/while-true-do/ansible-role-sys_vm_guest/issues)
or [Pull Requests](https://github.com/while-true-do/ansible-role-sys_vm_guest/pulls) after
reading the [Contribution Guideline](https://github.com/while-true-do/doc-library/blob/master/docs/CONTRIBUTING.md).

See who has contributed already in the [kudos.txt](./kudos.txt).

## License

This work is licensed under a [BSD-3-Clause License](https://opensource.org/licenses/BSD-3-Clause).

## Contact

-   Site <https://while-true-do.io>
-   Twitter <https://twitter.com/wtd_news>
-   Code <https://github.com/while-true-do>
-   Mail [hello@while-true-do.io](mailto:hello@while-true-do.io)
-   IRC [freenode, #while-true-do](https://webchat.freenode.net/?channels=while-true-do)
-   Telegram <https://t.me/while_true_do>
