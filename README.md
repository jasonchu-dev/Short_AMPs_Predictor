# Short Antimicrobial Peptides Prediction

Bio/chemoinformatics and machine learning project. Computational drug discovery based on QSAR made with Random Forest Classifier.

## Run
```
    pip install -r requirements.txt
```
CD-HIT and Pfeature not available on pip so must do this
```
    wget https://github.com/raghavagps/Pfeature/raw/master/PyLib/Pfeature.zip
    unzip Pfeature.zip
    cd Pfeature/
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
Remove duplicate peptides and convert to txt
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
When done, go back to lastest setuptools
```
    pip install --upgrade setuptools
```