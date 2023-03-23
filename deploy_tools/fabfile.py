import random
from fabric.contrib.files import append
from fabric.api import cd, env, run

REPO_URL = "https://github.com/pgodschalk/obey-the-testing-goat.git"


def deploy():
    site_folder = f"/home/{env.user}/{env.host}"
    run(f"mkdir --parents {site_folder}")
    with cd(site_folder):
        _get_latest_image()
        _create_or_update_dotenv()
        _update_static_files()
        _update_database()
        _restart_container()


def _get_latest_image():
    run("podman-compose pull")


def _create_or_update_dotenv():
    append(".env", "DJANGO_DEBUG_FALSE=y")
    append(".env", f"SITENAME={env.host}")
    current_contents = run("cat .env")
    if "DJANGO_SECRET_KEY" not in current_contents:
        new_secret = "".join(
            random.SystemRandom().choices("abcdefghijklmnopqrstuvwxyz0123456789", k=50)
        )
        append(".env", f"DJANGO_SECRET_KEY={new_secret}")


def _update_static_files():
    run("./collectstatic.sh")


def _update_database():
    run("podman-compose exec obey-the-testing-goat python manage.py migrate --noinput")


def _restart_container():
    run("podman-compose down")
    run("podman-compose up -d")
