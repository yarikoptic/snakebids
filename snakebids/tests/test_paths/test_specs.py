from snakebids.paths.specs import _find_entity, v0_0_0


def test_all_entries_define_entity():
    spec = v0_0_0()
    for item in spec:
        assert "entity" in item


def test_subject_dir_can_be_excluded():
    spec = v0_0_0(subject_dir=False)
    subject = _find_entity(spec, "sub")
    assert subject.get("dir") is False


def test_session_dir_can_be_excluded():
    spec = v0_0_0(session_dir=False)
    session = _find_entity(spec, "ses")
    assert session.get("dir") is False
