# Learning-Automation 🚀

This repository contains various automation scripts and a common library of functions used by these scripts. The repository is organized to facilitate easy access, modification, and execution of automation tasks.

## Getting Started 🌟

### Prerequisites 📋

Ensure you have the following installed:
- Python 3.x
- Pip (Python package installer)
- Jupyter Notebook (optional, for working with `lib.ipynb`)

### Setup 🛠️

1. **Clone the repository**
    ```sh
    git clone https://github.com/deepesh611/Learning-Automation.git
    cd Learning-Automation/src
    ```

2. **Run `setup.sh` to install dependencies**
    ```sh
    ./setup.sh
    ```

3. **Running the Script Selection**

    - **Using PowerShell (Administrator)**
    - You can create a shortcut of this file on the Desktop for ease of access, and perform `Run as Administrator` on Right-Click
        ```ps
        .\Script-Selection.ps1
        ```

    - **Create a shortcut**: You can create a shortcut of the file `Script-Selection.ps1` on your desktop for easy access.

## Usage 📚

1. **Adding New Scripts**

    - Place your new script files in the `Scripts` directory.
    - Ensure your scripts import the common library i.e `lib.py`.
  
      ```python
      import os
      import sys
      import importlib.util
      
      # Specify the module file path
      lib_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'lib', 'lib.py'))
      
      # Load the module
      spec = importlib.util.spec_from_file_location("lib", lib_path)
      lib = importlib.util.module_from_spec(spec)
      sys.modules["lib"] = lib
      spec.loader.exec_module(lib)
      ```

2. **Modifying the Common Library**

    - Add or modify functions in `lib.py`.
    - If you're working in a Jupyter environment, update `lib.ipynb` accordingly.
    - Always ensure changes are reflected in both `lib.py` and `lib.ipynb`.

## Contributing 🤝

Contributions are always appreciated. Here are some guidelines to help you get started:

1. Fork the repository and create your branch from `main`.
2. If you've added code that should be tested, add tests.
3. If you've changed any scripts or the common library, update the documentation.
4. Ensure the new code or scripts follow the existing style and format.
5. Update both `lib.py` and `lib.ipynb` when modifying the common library functions.
6. Make sure that you have given proper description in your PR
7. Include your GitHub profile picture and name in the contributors section below.

## Contributors ✨

Thanks goes to these wonderful people:

<!-- prettier-ignore -->
<table>
  <tr>
    <td align="center"><a href="https://github.com/deepesh611"><img src="https://avatars.githubusercontent.com/u/deepesh611?v=4" width="100px;" alt=""/><br /><sub><b>Deepesh Patil</b></sub></a><br /></td>
    <!-- Add more contributors here -->
  </tr>
</table>

## License 📄

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
