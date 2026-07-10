from src.models.reports.report import Report

def test_report_created():
    report = Report()
    assert report is not None

def test_generate_report():
    report = Report()
    result = report.generate(120)
    assert isinstance(result, str)

def test_report_contains_aqi():
    report = Report()
    result = report.generate(120)
    assert "120" in result