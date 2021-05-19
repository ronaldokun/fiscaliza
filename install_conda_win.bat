call conda create -n test python=3.8 -y

call conda activate test

call conda install -c intel libpython m2w64-toolchain -y

echo [build] > %CONDA_PREFIX%\Lib\distutils\distutils.cfg

echo compiler = mingw32 >> %CONDA_PREFIX%\Lib\distutils\distutils.cfg

call python -m pip install -r requirements.txt

call python -m pip install -i https://test.pypi.org/simple/ fiscaliza

