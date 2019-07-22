from fabric import Connection, Config, task

@task
def update(c):
    c.run("pwd")
    c.run("eval `ssh-agent` && ssh-add /home/muchogo/.ssh/sysadmin.pem")
    c.run("ansible-playbook -i hosts deploy.yml")
