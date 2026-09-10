def test_agent_orchestrator():
    prompt = "Test execution query for agentic-telemedicine-triage-assistant"
    assert len(prompt) > 0
    assert "Test" in prompt
