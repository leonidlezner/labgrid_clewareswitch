mkdir tmp
cd tmp
git clone https://github.com/flok99/clewarecontrol
cd clewarecontrol
make all
make cleware_python3
python setup.py install
