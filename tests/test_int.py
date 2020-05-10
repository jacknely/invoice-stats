import run
import pytest


def test_input_2(mocker, capsys):
    """ method for testing option 2 from start menu """
    mocker.patch("builtins.input", side_effect=["2", "70.00", "7"])
    run.main()
    captured = capsys.readouterr()
    captured = captured.out.split("\n")
    assert captured[-2] == "[70.0]"


def test_input_1(mocker, capsys):
    """ method for testing option 1 from start menu """
    mocker.patch("builtins.input", side_effect=["1", "100.00, 20.54", "7"])
    run.main()
    captured = capsys.readouterr()
    captured = captured.out.split("\n")
    assert captured[-2] == "[100.0, 20.54]"


def test_input_4(mocker, capsys):
    """ method for testing option 4 from start menu """
    mocker.patch("builtins.input", side_effect=["2", "70.00", "4", "7"])
    run.main()
    captured = capsys.readouterr()
    captured = captured.out.split("\n")
    assert captured[-2] == "The median is: 70.00"


def test_input_5(mocker, capsys):
    """ method for testing option 5 from start menu """
    mocker.patch("builtins.input", side_effect=["2", "70.00", "5", "7"])
    run.main()
    captured = capsys.readouterr()
    captured = captured.out.split("\n")
    assert captured[-2] == "The mean is: 70.00"


def test_input_3(mocker, capsys):
    """ method for testing option 3 from start menu """
    mocker.patch("builtins.input", side_effect=["2", "70.00", "3", "7"])
    run.main()
    captured = capsys.readouterr()
    print(captured.out)
    captured = captured.out.split("\n")
    assert captured[-1] == ""


if __name__ == "__main__":
    pytest.main()
