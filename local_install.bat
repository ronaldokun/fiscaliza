call conda deactivate

call conda env remove -n teste -y

call conda create -n teste python=3.8 -y

call conda activate teste

call python -m pip install -r requirements.txt

call python -m pip install -i https://test.pypi.org/simple/ fiscaliza
