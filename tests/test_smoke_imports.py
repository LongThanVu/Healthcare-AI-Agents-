def test_imports() -> None:
    from apps.api_gateway.app.main import app as _gateway_app
    from apps.orchestrator.app.main import app as _orchestrator_app
    from services.data_agent.app.main import app as _data_app
    from services.diagnosis_agent.app.main import app as _diagnosis_app
    from services.scheduling_agent.app.main import app as _scheduling_app

    assert _gateway_app is not None
    assert _orchestrator_app is not None
    assert _data_app is not None
    assert _diagnosis_app is not None
    assert _scheduling_app is not None
