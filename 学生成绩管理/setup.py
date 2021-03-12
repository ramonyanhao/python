from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
buildOptions = dict(packages = [], excludes = [])

base = 'Console'

executables = [
    Executable('student_score.py', base=base, targetName = 'student_score.exe',icon = "favicon.ico")
]

setup(name='student',
      version = '1.0',
      description = 'student',
      options = dict(build_exe = buildOptions),
      executables = executables)
