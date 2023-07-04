from agbenchmark.challenge import Challenge


def basic_read_file_mock(task: str, workspace: str) -> None:
    """
    This mock reads a file and returns its content.
    """

    file_contents = Challenge.open_file(workspace, "file_to_check.txt")

    Challenge.write_to_file(
        workspace, "file_to_check.txt", f"random string: {file_contents}"
    )


def basic_write_file_mock(task: str, workspace: str) -> None:
    """
    This mock writes to a file (creates one if it doesn't exist)
    """
    Challenge.write_to_file(
        workspace,
        "file_to_check.txt",
        "Washington DC is the capital of the United States of America",
    )


def basic_retrieval_mock(task: str, workspace: str) -> None:
    """
    This mock writes to a file (creates one if it doesn't exist)
    """
    Challenge.write_to_file(
        workspace,
        "file_to_check.txt",
        "25.89",
    )
