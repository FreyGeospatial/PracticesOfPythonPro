# PracticesOfPythonPro
Follows the tutorial found in Dane Hillard's "Practices of the Python Pro"

### Good practices:
When installing a project (as a package?),it is good practice to do so in "editable" mode, which will allow you to make changes to the project without having to uninstall and reinstall for those changes to take effect. To install a local project in editable mode, run `py -m pip install -e .` while in the directory with the "pyproject.toml" or "requirements.txt" file.
