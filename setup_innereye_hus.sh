curl -s https://packagecloud.io/install/repositories/github/git-lfs/script.deb.sh | sudo bash
sudo apt-get install git-lfs
git lfs install
git lfs pull
conda env create --file environment.yml
conda activate InnerEye
export PYTHONPATH=`pwd`
