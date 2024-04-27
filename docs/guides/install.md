# Installation

---

## Installers

=== "macOS"
=== "GUI Installer"
=== "Command line installer"

=== "Windows"
=== "GUI Installer"
=== "Command line installer"

## pip

CheckConnect is available on PyPI and can be installed with [pip](https://pip.pypa.io).

    ```
    pip install checkconnect
    ```

!!! warning
This method modifies the Python environment in which you choose to install. Consider instead using [pipx](#pipx) to avoid dependency conflicts.

## pipx

[pipx](https://github.com/pypa/pipx) allows for the global installation of Python applications in isolated environments.

    ```
    pipx install checkconnect
    ```


    ```
    sudo dnf install hatch
    ```

    ## Void Linux

    ```
    xbps-install hatch
    ```

    ## Build system availability

    Hatchling is Hatch's [build backend](config/build.md#build-system) which you will never need to install manually. See its [changelog](history/hatchling.md) for version information.

    [![Packaging status](https://repology.org/badge/vertical-allrepos/hatchling.svg){ loading=lazy .off-glb }](https://repology.org/project/hatchling/versions)
