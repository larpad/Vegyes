from setuptools import setup, find_packages

setup(
    name="your-app-name",
    version="0.1",
    packages=find_packages(),
)


# Setup.py for Multiple Entry Points

# from setuptools import setup, find_packages

# # Lista az összes alkalmazásról és azok belépési pontjairól
# APPLICATIONS = {
#     "app1": {
#         "module": "src.app1.main",
#         "function": "main",
#         "name": "First Application",
#         "description": "This is the first application"
#     },
#     "app2": {
#         "module": "src.app2.main",
#         "function": "main",
#         "name": "Second Application",
#         "description": "This is the second application"
#     },
#     "utility": {
#         "module": "src.utils.data_processor",
#         "function": "main",
#         "name": "Data Processor Utility",
#         "description": "Utility for processing data"
#     }
# }

# # Entry pointok generálása
# console_scripts = [
#     f"{app_id}={app_info['module']}:{app_info['function']}"
#     for app_id, app_info in APPLICATIONS.items()
# ]

# setup(
#     name="multi-app-package",
#     version="0.1.0",
#     author="Your Name",
#     author_email="your.email@example.com",
#     description="Package containing multiple applications",
#     long_description=open("README.md").read(),
#     long_description_content_type="text/markdown",
#     packages=find_packages(where="src"),
#     package_dir={"": "src"},
#     python_requires=">=3.6",
#     install_requires=[
#         "requests>=2.25.1",
#         # további függőségek...
#     ],
#     entry_points={
#         "console_scripts": console_scripts,
#     },
#     # További metaadatok...
# )