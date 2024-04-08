from celery import shared_task
from upcoming_matches import get_upcomin_matches

@shared_task
def run_get_upcomin_matches():
    get_upcomin_matches("https://www.rugbypass.com/fixtures/")