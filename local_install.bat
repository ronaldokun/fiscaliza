call conda deactivate

call conda env remove -n fiscaliza -y

call conda create -n fiscaliza python=3.8 -y

call conda activate fiscaliza

call python -m pip install -r requirements.txt

call python -m pip install -i https://test.pypi.org/simple/ fiscaliza
