from django.core.management.base import BaseCommand
import time
from core.scraper import scrape_merolagani_news

class Command(BaseCommand):
    help = 'Runs news crawler automatically'

    def handle(self, *args, **kwargs):
        self.stdout.write("Starting Crawler Loop...")
        while True:
            self.stdout.write("Fetching latest news...")
            scrape_merolagani_news()
            time.sleep(30) # Har 30 sec ma auto-fetch