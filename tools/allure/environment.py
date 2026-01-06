import platform
import sys

from config import settings


def create_allure_environment_file():
    # Create a list of elements in the format {key}={value}
    items = [f'{key}={value}' for key, value in settings.model_dump(mode="json").items()]
    items.append(f'os_info={platform.system()}, {platform.release()}')
    items.append(f'python_version={sys.version}')
    # Collect all the elements into a single line with hyphens
    properties = '\n'.join(items)

    # Open the ./allure-results/environment.properties file for reading
    with open(settings.allure_results_dir.joinpath('environment.properties'), 'w+') as file:
        file.write(properties)  # Write variables to a file