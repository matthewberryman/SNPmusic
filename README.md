# SNPmusic

## Description
Turns your SNP data into music.

## Software requirements
Install Python 3.x.
Install the packages from requirements.txt file, e.g.
```shell
pip3 install -r requirements.txt
```

## Data requirements
* Download the .fa.gz files from [here](https://ftp.ncbi.nlm.nih.gov/genomes/archive/old_genbank/Eukaryotes/vertebrates_mammals/Homo_sapiens/GRCh37/Primary_Assembly/assembled_chromosomes/FASTA/) and place them in the same directory as the code and gunzip them all e.g. `gunzip *.fa.gz`
* Put the .txt version of your 23andMe data in same directory

## Running it
```shell
python3 snpmusic.py your_genome_file.txt
```
