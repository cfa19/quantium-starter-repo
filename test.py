import pytest
from dash.testing.application_runners import DashRunner
from task4 import app  

@pytest.fixture
def dash_duo_runner():
    """Provides the Dash testing framework runner."""
    runner = DashRunner(app)
    yield runner
    runner.stop()

def test_header_present(dash_duo_runner):
    dash_duo_runner.start_server()
    header = dash_duo_runner.find_element("h1")
    assert header.text == "Soul Foods Sales Visualiser", "Header text does not match."

def test_visualisation_present(dash_duo_runner):
    dash_duo_runner.start_server()
    visualisation = dash_duo_runner.find_element("#sales-graph")
    assert visualisation is not None, "The visualization graph is missing."

def test_region_picker_present(dash_duo_runner):
    dash_duo_runner.start_server()
    region_picker = dash_duo_runner.find_element("#region-filter")
    assert region_picker is not None, "Region picker is not found on the page."
