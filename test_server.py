import pytest
from threading import Thread
from server import app  # Importiere die Microdot-App
from playwright.async_api import async_playwright


# Fixture: Starte den Microdot-Server in einem separaten Thread
@pytest.fixture(scope="module", autouse=True)
def start_server():
    server_thread = Thread(target=lambda: app.run(port=8000), daemon=True)
    server_thread.start()


# Test für die Benutzeroberfläche
@pytest.mark.asyncio
async def test_button_click():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)  # Headless-Browser
        page = await browser.new_page()

        # Lade die Webseite
        await page.goto("http://localhost:8000/")

        # Überprüfe die Überschrift
        headline_text = await page.text_content("#main-headline")
        assert headline_text == "Welcome to end to end testing"

        # Überprüfe den Button-Text
        button_text = await page.text_content("#my-button")
        assert "Click me" in button_text

        # Simuliere einen Klick auf den Button
        await page.click("#my-button")

        # Überprüfe die Textänderung
        output_text = await page.text_content("#output")
        assert output_text == "Button was clicked!"

        await browser.close()
