from fabric import task


@task
def update(c):
    c.run("eval `ssh-agent` && ssh-add /home/muchogo/.ssh/sysadmin.pem")
    c.run("ansible-playbook -i hosts provision.yml")
