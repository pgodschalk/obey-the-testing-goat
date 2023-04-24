from fabric.api import run
from fabric.context_managers import settings, shell_env


def _get_manage_dot_py(host):
    parsed_host = host.replace(".", "")
    return f"podman exec {parsed_host}_obey-the-testing-goat_1 python manage.py"


def reset_database(host):
    manage_dot_py = _get_manage_dot_py(host)
    with settings(host_string=f"patrick@{host}"):
        run(f"{manage_dot_py} flush --noinput")


def _get_server_env_vars(host):
    env_lines = run(f"cat ~/obey-the-testing-goat/{host}/.env").splitlines()
    return dict(line.split("=") for line in env_lines if line)


def create_session_on_server(host, email):
    manage_dot_py = _get_manage_dot_py(host)
    with settings(host_string=f"patrick@{host}"):
        env_vars = _get_server_env_vars(host)
        with shell_env(**env_vars):
            session_key = run(f"{manage_dot_py} create_session {email}")
            return session_key.strip()
