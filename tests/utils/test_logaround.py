from src.utils.logaround import log_around


def test_log_around_preserves_function_name()-> None:

    @log_around
    def sample(value: int) -> int:
        return value + 1

    assert sample.__name__ == "sample"
    assert sample(value=1) == 2