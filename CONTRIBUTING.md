# Contributing to TextInsights

Thank you for considering contributing to TextInsights! This document provides guidelines and instructions for contributing to this project.

## Code of Conduct

By participating in this project, you agree to maintain a respectful and inclusive environment for everyone.

## Getting Started

### Development Setup

1. Fork the repository on GitHub
2. Clone your fork locally:
   ```bash
   git clone https://github.com/your-username/textinsights.git
   cd textinsights
   ```
3. Create a virtual environment:
   ```bash
   python -m venv venv
   ```
4. Activate the environment:
   - Windows: `venv\Scripts\activate`
   - macOS/Linux: `source venv/bin/activate`
5. Install development dependencies:
   ```bash
   pip install -r requirements-dev.txt
   ```
6. Install the package in editable mode:
   ```bash
   pip install -e .
   ```

### Development Workflow

1. Create a branch for your feature or bugfix:
   ```bash
   git checkout -b feature-name
   ```
2. Make your changes
3. Format your code:
   ```bash
   black textinsights tests
   isort textinsights tests
   ```
4. Run linting:
   ```bash
   flake8 textinsights tests
   ```
5. Run tests:
   ```bash
   pytest
   pytest --cov=textinsights  # For coverage report
   ```
6. Commit your changes:
   ```bash
   git commit -m "Add feature"
   ```
7. Push to your fork:
   ```bash
   git push origin feature-name
   ```
8. Create a Pull Request from your fork to the original repository

## Pull Request Guidelines

- Fill in the provided Pull Request template
- Include tests for new features
- Update documentation if needed
- Ensure all tests pass and linting issues are resolved
- Keep Pull Requests focused on a single change
- Reference any relevant issues

## Style Guidelines

We follow these style guidelines:

### Python Code Style

- We use [Black](https://black.readthedocs.io/) for code formatting
- We use [isort](https://pycqa.github.io/isort/) for import sorting
- We use [flake8](https://flake8.pycqa.org/) for linting

### Docstrings

We use Google-style docstrings:

```python
def function(arg1, arg2):
    """One-line summary of function.

    More detailed explanation of the function.

    Args:
        arg1 (int): Description of arg1
        arg2 (str): Description of arg2

    Returns:
        bool: Description of return value
        
    Raises:
        ValueError: When something goes wrong
    """
    return True
```

### Commit Messages

- Use present tense ("Add feature" not "Added feature")
- First line is a summary (max 50 characters)
- Reference issues and pull requests if needed

## Testing

- Write tests for all new features and bug fixes
- Aim for high code coverage
- Place tests in the `tests/` directory, mirroring the package structure
- Use pytest for running tests

## Documentation

- Update the README.md if necessary
- Add docstrings to all public functions, classes, and methods
- Consider adding examples for complex functionality

## Feature Requests

We welcome feature requests! Please create an issue with the "enhancement" label and:

- Clearly describe the feature
- Explain the benefit
- Provide examples of how it would be used

## Reporting Bugs

When reporting bugs, please include:

- Steps to reproduce the bug
- Expected behavior
- Actual behavior
- TextInsights version
- Python version
- Operating system

## Releasing (For Maintainers)

1. Update version in `textinsights/__init__.py`
2. Update CHANGELOG.md
3. Create a new tag:
   ```bash
   git tag v0.1.0
   git push origin v0.1.0
   ```
4. Build the package:
   ```bash
   python -m build
   ```
5. Upload to PyPI:
   ```bash
   twine upload dist/*
   ```

## License

By contributing, you agree that your contributions will be licensed under the project's MIT License.