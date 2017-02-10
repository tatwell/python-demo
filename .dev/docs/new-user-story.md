# New User Story

## Checklist

When starting a new Trello user story card, add the following comment:

    **New User Story Checklist**

    - Set branch and version.
    - Define acceptance criteria.
    - Task story.
    - Add tasks for new issues.
      - Count: 0
      - Added 0 tasks.

    - Task TODO / FIXME code comments.
      - Count: 0
      - Added 0 tasks.

    - Run tests.
    ```
    Ran 4 tests in 11.460s
    OK
    ```

    - Check git status.


## Tasks

1. Set branch, version, and datastore reset.

In card description:

- Branch: `fkfi8x0y-redesigned-home-page`
- Version: `fkfi8x0y`

2. Define acceptance criteria in Card Description.

3. Add new Tasks checklist.

First task should be:

    Create branch `fkfi8x0y-redesigned-home-page` and update `app.yaml` version.

4. Check repository issues.

Check here and add any small new issues as tasks:

- https://github.com/tatwell/python-demo/issues

5. Grep repository for TODO / FIXME tasks:

    # Count: -I excludes binary files.
    egrep --exclude-dir='lib' -I -Rni 'TODO|FIXME' ~/projects/tatwell-python-demo/app-engine | wc -l

    # List
    egrep --exclude-dir='lib' -I -Rni 'TODO|FIXME' ~/projects/tatwell-python-demo/app-engine | less

6. Run tests.

    cd ~/projects/tatwell-python-demo/app-engine
    nosetests -c nose.cfg

7. Check git status in repository.

    git status
    git branch

There should be no uncommited changes. Only `master` and `dev` branches should be open. Close any others.
