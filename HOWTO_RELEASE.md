# How to Release

Step-by-step guide to cutting a new release.

## Pre-release

1. update version in ``setup.py``

2. update version in ``astrolabels/__init__.py``

3. update ``README.md`` if necessary

4. confirm all tests pass & flake8 gives no errors
  ```
  $ cd astrolabels/
  $ nosetests
  $ flake8 --ignore N802,N806 `find . -name \*.py | grep -v setup.py`
  ```

5. create a release tag; e.g.
   ```
   $ git tag -a v0.1 -m 'version 0.1 release'
   ```

6. push the commits and tag to github; e.g.

  ```
  $ git push origin v0.1
  $ git push origin master
  ```

7. under "tags" on github, update the release notes

8. push the new release to PyPI:
   ```
   $ python setup.py sdist upload
   ```


## Post-release

1. update version in ``setup.py`` to next version; e.g. '0.1-git'

2. update version in ``clusterlensing/__init__.py`` to the same
