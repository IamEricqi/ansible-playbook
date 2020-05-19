---
- hosts: all
  remote_user: root
  tasks:
    - name: Check date
      command: date
    - name: Check ip
      command: ip add
