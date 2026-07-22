from failure_atlas.core import FailureAtlas

def test_failure_atlas_loading():
    atlas = FailureAtlas()
    failures = atlas.get_all_failures()
    assert len(failures) >= 7

def test_search_by_domain():
    atlas = FailureAtlas()
    robotics_failures = atlas.search_by_domain("Robotics")
    assert len(robotics_failures) >= 2
    for f in robotics_failures:
        assert f['domain'] == "Robotics"

def test_search_keyword():
    atlas = FailureAtlas()
    results = atlas.search_keyword("I2C")
    assert len(results) >= 1
    assert any("I2C" in r['title'] or "I2C" in r['root_cause'] for r in results)

def test_filter_by_severity():
    atlas = FailureAtlas()
    critical_failures = atlas.filter(severity="Critical")
    assert len(critical_failures) >= 2
    for f in critical_failures:
        assert f['severity'] == "Critical"

def test_export_markdown_summary():
    atlas = FailureAtlas()
    md = atlas.export_markdown_summary()
    assert "# 📖 Failure Atlas" in md
    assert "FAIL-ROB-001" in md
