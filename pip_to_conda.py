# %%
def pip_to_conda(requirements_txt):
  """Converts a pip requirements.txt file to a conda environment.yml file.

  Args:
    requirements_txt: The path to the pip requirements.txt file.

  Returns:
    A string containing the conda environment.yml file content.
  """

  try:
    with open(requirements_txt, 'r') as f:
      pip_requirements = f.readlines()
  except FileNotFoundError:
    return "Error: requirements.txt file not found."

  conda_requirements = []
  pip_only_packages = []

  for req in pip_requirements:
    req = req.strip()
    if req and not req.startswith('#'):  # Ignore empty lines and comments
      try:
        # Try to find the package on conda-forge
        conda_package = req.split('==')[0]  # Extract package name
        conda_requirements.append(f'- conda-forge/{conda_package}')
      except IndexError:
        pip_only_packages.append(req)

  conda_env = {
      'name': 'my_conda_env',  # Choose your environment name
      'channels': ['conda-forge', 'defaults'],
      'dependencies': conda_requirements
  }

  if pip_only_packages:
    conda_env['dependencies'].append({'pip': pip_only_packages})

  import yaml
  return yaml.dump(conda_env, indent=2)

if __name__ == "__main__":
  """Example usage."""
  requirements_file = "requirements.txt"
  conda_env_content = pip_to_conda(requirements_file)
  print(conda_env_content)
# %%
