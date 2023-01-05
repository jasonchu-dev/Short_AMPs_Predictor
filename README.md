# Short Antimicrobial Peptides Prediction

Bio/chemoinformatics and machine learning project

## Stuff needed
* scikit-learn
* Pfeature
* Lazy Predict
* pandas
* Matplotlib
* seaborn
* CD-HIT
* setuptools 58.2.0
* Conda

## Run
Need conda. CD-HIT and Pfeature not available on pip so must do this
```
    wget https://github.com/raghavagps/Pfeature/raw/master/PyLib/Pfeature.zip
    unzip Pfeature.zip
    cd Pfeature/
    pip install setuptools==58.2.0
    pip install lazypredict
    python setup.py install
    conda install -c bioconda cd-hit -y
    cd ..
```
Get dataset
```
    wget https://sourceforge.net/projects/axpep/files/Deep-AmPEP30_datasets/deep-ampep30-train_set.zip
    wget https://sourceforge.net/projects/axpep/files/Deep-AmPEP30_datasets/deep-ampep30-test_set.zip
    unzip deep-ampep30-train_set.zip
    unzip deep-ampep30-test_set.zip
```
Remove duplicate peptides (latest dataset should have no duplicate data but optional)
```
    cd train_set/
    cd-hit -i train_po.fasta -o po_cd_hit.txt -c 0.99
    cd-hit -i train_ne.fasta -o ne_cd_hit.txt -c 0.99
    cd ..
    cd test_set/
    cd-hit -i test_po.fasta -o po_cd_hit.txt -c 0.99
    cd-hit -i test_ne.fasta -o ne_cd_hit.txt -c 0.99
    cd ..
```