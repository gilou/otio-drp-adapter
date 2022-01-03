# OpenTimelineIO drp adapter plugin

This repository aims at storing an adapter for the OpenTimelineIO project allowing to import .drp files from the Blackmagic ATEM ISO. The initial goal is to be able to import them directly in KDEnlive.

## Licensing

This plugin is licensed under the
[Apache License, Version 2.0](https://www.apache.org/licenses/LICENSE-2.0.txt)


## Testing your plugin during development
```bash
# In the root folder of the repo
pip install -e .

# Test an adapter for instance
otioconvert -i some_timeline.drp -o some_timeline.ext
```

## Unit tests

It's always a good idea to write unit tests for you code.
Please provide tests that run against supported versions of python and 
OpenTimelineIO.


## Github Actions

A set of simple automation scripts are available in the `.github/workflows` folder.
* `ci.yaml` - runs unit tests
* `create_draft_release` - when a tag is pushed, it creates a draft for a release
* `deploy_package.yaml` - simple packing an publishing of a plugin package. 
  Make sure you have a valid token for your PyPi user added to your repos 
  [secrets](https://docs.github.com/es/actions/reference/encrypted-secrets).


## Upload to PyPi

Should you want to release your package to the world and let others reap the 
fruits of your labor, an example setup.py is provided which should guide you 
on the way towards publishing your plugin on PyPi.
There's also a sample github-action provided to help automate the process.

Manual steps for creating a simple package and upload to (test)PyPi:
```bash
python setup.py sdist bdist_wheel --universal
twine upload --repository testpypi dist/*
```
Please check out pythons [docs](https://packaging.python.org/tutorials/packaging-projects/#packaging-python-projects) 
for more detailed descriptions on packaging. 


## Let us know about your plugin
If you release your plugin to the public please let us know about it, so we can 
add it to our [list](https://github.com/PixarAnimationStudios/OpenTimelineIO/wiki/Tools-and-Projects-Using-OpenTimelineIO) 
of known plugins.


## Contributions

If you have any suggested changes to the template repository itself, 
please provide them via [pull request](../../pulls) or [create an issue](../../issues) as appropriate. 

All contributions back to the template repository must align with the contribution
[guidelines](https://opentimelineio.readthedocs.io/en/latest/tutorials/contributing.html) 
of the OpenTimelineIO project.
