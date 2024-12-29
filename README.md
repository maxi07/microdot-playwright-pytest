# Microdot Playwright End-To-End (E2E) Tests
With the amazing [Microdot](https://github.com/miguelgrinberg/microdot) project, I wrote a sample project on how to have End-To-End Tests for MicroDot projects. In my case, I use Microdot on a [Raspberry Pico W](https://www.raspberrypi.com/documentation/microcontrollers/pico-series.html#picow-technical-specification) and always wanted to have automated testig for CI. This project uses [Playwright](https://playwright.dev) and [Pytest](https://docs.pytest.org/en/stable/) for automated UI testing. 


## Requirements
Run the following two commands:
```bash
pip install -r requirements.txt
playwright install
```

## Run the test locally
You can run the tests locally, for testing without a Raspberry Pico. After installing the requirements, run 
```python
pytest test_server.py
```