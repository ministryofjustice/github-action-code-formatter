import pytest
import importlib
python_malformed_yaml_main = importlib.import_module("python-malformed-yaml.main")
main = python_malformed_yaml_main.main


expected_exception = 'Malformed YAML detected:\n\ntest/test_python_malformed_yaml/test_yaml_files/bad_2.yml:\nwhile scanning a quoted scalar\n  in "test/test_python_malformed_yaml/test_yaml_files/bad_2.yml", line 2, column 14\nfound unexpected end of stream\n  in "test/test_python_malformed_yaml/test_yaml_files/bad_2.yml", line 3, column 1\n\ntest/test_python_malformed_yaml/test_yaml_files/bad_1.yml:\nwhile scanning a quoted scalar\n  in "test/test_python_malformed_yaml/test_yaml_files/bad_1.yml", line 2, column 6\nfound unexpected end of stream\n  in "test/test_python_malformed_yaml/test_yaml_files/bad_1.yml", line 3, column 1\n Please correct and resubmit this PR.'

def test_exception():
    with pytest.raises(Exception) as exc_info:   
        main()   
    assert str(exc_info.value) == expected_exception