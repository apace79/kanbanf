Running on windows
------------------

cmd /C "set KANBANF_INST=dev&& pipenv run python runner.py"

cmd /C "set KANBANF_INST=dev&& set FLASK_APP=runner.py&& set FLASK_DEBUG=1&& pipenv run flask run"


Test
----
pipenv run python -m pytest

* to stop at first failure:
  pipenv run python -m pytest -x 
* tests should start with "test_"